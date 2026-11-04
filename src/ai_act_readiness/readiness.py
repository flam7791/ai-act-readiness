"""Readiness: classification x evidence -> gaps, deadlines and the decisions an executive committee owns."""
from __future__ import annotations

import csv
import json
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

from .classify import (DEROGATION, HIGH_RISK, INSUFFICIENT, MINIMAL, PROHIBITED, TRANSPARENCY,
                       Classification, classify, load_rules)

EVIDENCE_STATES = {"done", "partial", "missing"}
RED, AMBER, GREEN = "red", "amber", "green"


@dataclass
class ObligationStatus:
    id: str
    title: str
    ref: str
    due: date
    evidence: str
    evidence_ref: str
    days_left: int

    @property
    def overdue(self) -> bool:
        return self.days_left < 0 and self.evidence != "done"


@dataclass
class UseCaseReadiness:
    uc: dict
    classification: Classification
    obligations: list[ObligationStatus]
    rag: str
    actions: list[str] = field(default_factory=list)


@dataclass
class LiteracyRow:
    role_group: str
    in_scope: int
    completed: int
    measures: str
    operates_high_risk: bool

    @property
    def coverage(self) -> float:
        return self.completed / self.in_scope if self.in_scope else 0.0


@dataclass
class Portfolio:
    as_of: date
    rules: dict
    use_cases: list[UseCaseReadiness]
    literacy: list[LiteracyRow]
    literacy_target: float
    data_issues: list[str]


def load_portfolio(path: Path) -> list[dict]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return data["use_cases"]


def load_evidence(path: Path, issues: list[str]) -> dict[tuple[str, str], tuple[str, str]]:
    out: dict[tuple[str, str], tuple[str, str]] = {}
    with open(path, newline="", encoding="utf-8") as f:
        for i, row in enumerate(csv.DictReader(f), start=2):
            status = (row.get("status") or "").strip().lower()
            if status not in EVIDENCE_STATES:
                issues.append(f"evidence.csv row {i}: status '{row.get('status')}' is not done, partial or missing; "
                              "treated as missing")
                status = "missing"
            if status == "done" and not (row.get("evidence_ref") or "").strip():
                issues.append(f"evidence.csv row {i}: marked done with no evidence reference; treated as partial")
                status = "partial"
            out[(row["use_case_id"].strip(), row["obligation_id"].strip())] = (status, (row.get("evidence_ref") or "").strip())
    return out


def load_literacy(path: Path, issues: list[str]) -> list[LiteracyRow]:
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        for i, row in enumerate(csv.DictReader(f), start=2):
            try:
                n, done = int(row["staff_in_scope"]), int(row["completed"])
            except (KeyError, ValueError):
                issues.append(f"literacy.csv row {i}: staff_in_scope and completed must be whole numbers; row skipped")
                continue
            if done > n:
                issues.append(f"literacy.csv row {i}: completed ({done}) exceeds staff in scope ({n}); capped")
                done = n
            rows.append(LiteracyRow(row["role_group"], n, done, row.get("measures", ""),
                                    (row.get("operates_high_risk") or "").strip().lower() == "yes"))
    return rows


def _rag(c: Classification, obs: list[ObligationStatus]) -> str:
    if c.category == PROHIBITED or any(o.overdue for o in obs):
        return RED
    if c.category == INSUFFICIENT or c.legal_review or any(o.evidence != "done" for o in obs):
        return AMBER
    return GREEN


def _actions(c: Classification, obs: list[ObligationStatus]) -> list[str]:
    if c.category == PROHIBITED:
        return ["Stop the use, or redesign it so the prohibited element is removed; record the decision."]
    if c.category == INSUFFICIENT:
        return ["Complete the screening questions before any classification is proposed."]
    acts = []
    if c.legal_review:
        acts.append("Legal review of the Art. 6(3) derogation; until confirmed, plan as high-risk.")
    over = [o for o in obs if o.overdue]
    if over:
        acts.append("Close overdue obligations now: " + ", ".join(o.id for o in over) + ".")
    open_ = [o for o in obs if not o.overdue and o.evidence != "done"]
    if open_:
        first = min(o.due for o in open_)
        acts.append(f"Fund and plan {len(open_)} open obligation" + ("" if len(open_) == 1 else "s")
                    + f", first due {first.isoformat()}.")
    return acts


def build(portfolio_path: Path, evidence_path: Path, literacy_path: Path, as_of: date,
          literacy_target: float = 0.8) -> Portfolio:
    rules = load_rules()
    issues: list[str] = []
    evidence = load_evidence(evidence_path, issues)
    seen: set[str] = set()
    out = []
    for uc in load_portfolio(portfolio_path):
        uid = uc.get("id")
        if not uid or uid in seen:
            issues.append(f"portfolio: use case without id or duplicate id '{uid}'; skipped")
            continue
        seen.add(uid)
        c = classify(uc, rules)
        obs = []
        for ob in c.obligations:
            status, ref = evidence.get((uid, ob.id), ("missing", ""))
            obs.append(ObligationStatus(ob.id, ob.title, ob.ref, ob.due, status, ref, (ob.due - as_of).days))
        out.append(UseCaseReadiness(uc, c, obs, _rag(c, obs), _actions(c, obs)))
    applicable = {(u.uc["id"], o.id) for u in out for o in u.obligations}
    for (uid, oid) in evidence:
        if uid not in seen:
            issues.append(f"evidence.csv: row for unknown use case '{uid}' ({oid}) ignored")
        elif (uid, oid) not in applicable:
            issues.append(f"evidence.csv: {uid} has evidence for {oid}, which does not apply to its proposed "
                          "category; ignored (check the screening or the evidence row)")
    return Portfolio(as_of, rules, out, load_literacy(literacy_path, issues), literacy_target, issues)


CATEGORY_ORDER = [PROHIBITED, HIGH_RISK, DEROGATION, TRANSPARENCY, MINIMAL, INSUFFICIENT]
