"""Render the readiness pack: Markdown for the executive committee, JSON for other tools."""
from __future__ import annotations

import json
from collections import Counter

from .classify import HIGH_RISK, INSUFFICIENT, PROHIBITED
from .readiness import AMBER, CATEGORY_ORDER, GREEN, RED, Portfolio

DOT = {RED: "RED", AMBER: "AMBER", GREEN: "GREEN"}


def _n(k: int, word: str) -> str:
    return f"{k} {word}" + ("" if k == 1 else "s")


def _months(days: int) -> str:
    return f"{days / 30.44:.0f} months" if days >= 0 else f"{-days} days overdue"


def decisions(p: Portfolio) -> list[str]:
    ucs = p.use_cases
    out = []
    prohib = [u for u in ucs if u.classification.category == PROHIBITED]
    if prohib:
        out.append("**Stop or redesign** " + ", ".join(f"{u.uc['id']} ({u.uc['name']})" for u in prohib)
                   + ": the screening matches a prohibited practice, applicable since 2 February 2025.")
    overdue = [(u, [o for o in u.obligations if o.overdue]) for u in ucs if u.classification.category != PROHIBITED]
    overdue = [(u, os) for u, os in overdue if os]
    if overdue:
        out.append("**Close overdue obligations now:** " + "; ".join(
            f"{u.uc['id']} {', '.join(o.id + ' (' + o.ref + ')' for o in os)}" for u, os in overdue) + ".")
    review = [u for u in ucs if u.classification.legal_review]
    if review:
        out.append("**Ask counsel to confirm the Art. 6(3) derogation** for " + ", ".join(u.uc["id"] for u in review)
                   + "; plan as high-risk until it is confirmed.")
    hr = [u for u in ucs if u.classification.category == HIGH_RISK]
    if hr:
        open_ = sum(1 for u in hr for o in u.obligations if o.evidence != "done")
        total = sum(len(u.obligations) for u in hr)
        due = min(o.due for u in hr for o in u.obligations)
        out.append(f"**Fund the high-risk programme:** {_n(len(hr), 'system')}, {open_} of {total} obligations open, "
                   f"first due {due.day} {due.strftime('%B %Y')} ({_months((due - p.as_of).days)} left).")
    insuff = [u for u in ucs if u.classification.category == INSUFFICIENT]
    if insuff:
        out.append("**Complete the screening** for " + ", ".join(u.uc["id"] for u in insuff)
                   + " before it progresses: no category is proposed on missing answers.")
    low = [r for r in p.literacy if r.coverage < p.literacy_target]
    if low:
        hi = [r for r in low if r.operates_high_risk]
        txt = ", ".join(f"{r.role_group} {r.coverage:.0%}" for r in (hi or low))
        out.append(f"**AI literacy:** {_n(len(low), 'role group')} below the {p.literacy_target:.0%} internal target"
                   + (f", including staff who operate high-risk systems ({txt})." if hi else f" ({txt})."))
    return out


def markdown(p: Portfolio, organisation: str) -> str:
    ucs = p.use_cases
    L = [f"# AI Act readiness: {organisation}", "",
         f"As of {p.as_of.isoformat()}. Rules: {p.rules['basis']}; dates checked {p.rules['checked']}.", "",
         "> Classification proposals for legal review, not legal advice. Every line below shows the screening "
         "answers and articles it rests on, so it can be challenged.", "",
         "## Decisions for the executive committee", ""]
    L += [f"{i}. {d}" for i, d in enumerate(decisions(p), 1)] or ["No decision needed this cycle."]
    cats = Counter(u.classification.category for u in ucs)
    rags = Counter(u.rag for u in ucs)
    L += ["", "## Portfolio at a glance", "",
          f"{len(ucs)} use cases: " + ", ".join(f"{cats[c]} {c}" for c in CATEGORY_ORDER if cats[c]) + ". "
          f"Status: {rags[RED]} red, {rags[AMBER]} amber, {rags[GREEN]} green.", "",
          "| Use case | Unit | Role | Proposed category | Status | Open obligations | Next due |",
          "|---|---|---|---|---|---|---|"]
    order = {RED: 0, AMBER: 1, GREEN: 2}
    for u in sorted(ucs, key=lambda u: (order[u.rag], u.uc["id"])):
        open_ = [o for o in u.obligations if o.evidence != "done"]
        nxt = min((o.due for o in open_), default=None)
        L.append(f"| {u.uc['id']} {u.uc['name']} | {u.uc.get('business_unit', '')} | "
                 f"{u.uc.get('role', '?').replace('_', ' ')} | {u.classification.category} | {DOT[u.rag]} | "
                 f"{len(open_)} of {len(u.obligations)} | {nxt.isoformat() if nxt else '-'} |")
    L += ["", "## AI literacy (Art. 4)", "", p.rules["literacy"]["note"], "",
          "| Role group | In scope | Completed | Coverage | Operates high-risk AI | Measures |", "|---|---|---|---|---|---|"]
    for r in p.literacy:
        flag = " (below target)" if r.coverage < p.literacy_target else ""
        L.append(f"| {r.role_group} | {r.in_scope} | {r.completed} | {r.coverage:.0%}{flag} | "
                 f"{'yes' if r.operates_high_risk else 'no'} | {r.measures} |")
    tot_in = sum(r.in_scope for r in p.literacy)
    tot_done = sum(r.completed for r in p.literacy)
    if tot_in:
        L.append(f"| **All** | {tot_in} | {tot_done} | {tot_done / tot_in:.0%} | | |")
    L += ["", "## Use case detail", ""]
    for u in sorted(ucs, key=lambda u: u.uc["id"]):
        c = u.classification
        L += [f"### {u.uc['id']} {u.uc['name']}: {c.category} ({DOT[u.rag]})", "",
              u.uc.get("purpose", ""), ""]
        L += [f"- {r}" for r in c.reasons]
        if u.actions:
            L += ["", "**Next:** " + " ".join(u.actions)]
        if u.obligations:
            L += ["", "| Obligation | Article | Due | Evidence | Days left |", "|---|---|---|---|---|"]
            for o in u.obligations:
                ev = o.evidence + (f" ({o.evidence_ref})" if o.evidence_ref else "")
                L.append(f"| {o.id} {o.title} | {o.ref} | {o.due.isoformat()} | {ev} | "
                         f"{'-' if o.evidence == 'done' else (str(o.days_left) + ' (overdue)' if o.overdue else o.days_left)} |")
        L.append("")
    L += ["## Data quality", ""]
    L += [f"- {x}" for x in p.data_issues] or ["No issues found in the input files."]
    L += ["", "## Basis", "", p.rules["note"], ""]
    return "\n".join(L)


def as_json(p: Portfolio, organisation: str) -> str:
    return json.dumps({
        "organisation": organisation, "as_of": p.as_of.isoformat(), "basis": p.rules["basis"],
        "decisions": decisions(p),
        "use_cases": [{
            "id": u.uc["id"], "name": u.uc["name"], "category": u.classification.category, "status": u.rag,
            "legal_review": u.classification.legal_review, "reasons": u.classification.reasons,
            "missing": u.classification.missing, "actions": u.actions,
            "obligations": [{"id": o.id, "ref": o.ref, "due": o.due.isoformat(), "evidence": o.evidence,
                             "days_left": o.days_left, "overdue": o.overdue} for o in u.obligations],
        } for u in p.use_cases],
        "literacy": [{"role_group": r.role_group, "in_scope": r.in_scope, "completed": r.completed,
                      "coverage": round(r.coverage, 3), "operates_high_risk": r.operates_high_risk}
                     for r in p.literacy],
        "data_issues": p.data_issues,
    }, indent=2, ensure_ascii=False)
