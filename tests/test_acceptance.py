"""Acceptance tests. Each test name starts with the backlog story it proves (docs/team/backlog.csv).

tools/trace.py fails CI if a story marked Done has no test here.
"""
from __future__ import annotations

import csv
import json
from datetime import date
from pathlib import Path

import pytest

from ai_act_readiness.classify import (DEROGATION, HIGH_RISK, INSUFFICIENT, MINIMAL, PROHIBITED, TRANSPARENCY,
                                       classify)
from ai_act_readiness.cli import main
from ai_act_readiness.readiness import AMBER, GREEN, RED, build
from ai_act_readiness.render import as_json, decisions, markdown

AS_OF = date(2026, 11, 4)
SAMPLE = Path(__file__).resolve().parent.parent / "data" / "sample"


def uc(**kw) -> dict:
    base = {"id": "T1", "name": "Test", "role": "provider_and_deployer", "prohibited_practice": None,
            "annex_iii_area": None, "profiling": False, "interacts_with_people": False,
            "generates_synthetic_content": False, "deepfake_published": False, "emotion_recognition": "none"}
    base.update(kw)
    return base


def ids(c) -> set[str]:
    return {o.id for o in c.obligations}


def write(tmp: Path, use_cases: list[dict], evidence: list[list], literacy: list[list] | None = None):
    p = tmp / "portfolio.json"
    p.write_text(json.dumps({"organisation": "Test Org", "use_cases": use_cases}), encoding="utf-8")
    e = tmp / "evidence.csv"
    with open(e, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["use_case_id", "obligation_id", "status", "evidence_ref", "owner_role"])
        w.writerows(evidence)
    lit = tmp / "literacy.csv"
    with open(lit, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["role_group", "staff_in_scope", "completed", "operates_high_risk", "measures"])
        w.writerows(literacy or [["Everyone", 10, 10, "no", "course"]])
    return p, e, lit


# US-01 ------------------------------------------------------------------------------------------
def test_US01_missing_answers_give_insufficient_not_minimal():
    c = classify({"id": "X", "role": "deployer", "prohibited_practice": None, "annex_iii_area": None})
    assert c.category == INSUFFICIENT
    assert "profiling" in c.missing and "emotion_recognition" in c.missing
    assert not c.obligations


def test_US01_unknown_codes_and_roles_are_not_guessed():
    assert classify(uc(annex_iii_area="9z_space")).category == INSUFFICIENT
    assert classify(uc(prohibited_practice="mind_reading")).category == INSUFFICIENT
    assert classify(uc(role="owner")).category == INSUFFICIENT


# US-02 ------------------------------------------------------------------------------------------
def test_US02_workplace_emotion_recognition_is_prohibited():
    c = classify(uc(emotion_recognition="workplace", interacts_with_people=True))
    assert c.category == PROHIBITED
    assert ids(c) == {"PROHIB"}
    assert any("Art. 5(1)(f)" in r for r in c.reasons)


def test_US02_declared_prohibited_practice_wins_over_annex_iii():
    c = classify(uc(prohibited_practice="social_scoring", annex_iii_area="5b_creditworthiness"))
    assert c.category == PROHIBITED and ids(c) == {"PROHIB"}


# US-03 ------------------------------------------------------------------------------------------
def test_US03_life_health_pricing_is_high_risk_with_fria():
    c = classify(uc(annex_iii_area="5c_life_health_insurance_pricing", profiling=True))
    assert c.category == HIGH_RISK
    assert {"HR-RISK", "HR-QMS", "HR-CONFORMITY", "DEP-FRIA"} <= ids(c)
    assert all(o.due == date(2027, 12, 2) for o in c.obligations)


def test_US03_recruitment_is_high_risk_without_fria_but_with_worker_information():
    c = classify(uc(annex_iii_area="4a_recruitment_selection", role="deployer", profiling=True))
    assert c.category == HIGH_RISK
    assert "DEP-FRIA" not in ids(c) and "DEP-WORKERS" in ids(c)


# US-04 ------------------------------------------------------------------------------------------
def test_US04_derogation_without_profiling_goes_to_legal_review():
    c = classify(uc(annex_iii_area="5c_life_health_insurance_pricing", derogation_ground="narrow_procedural_task"))
    assert c.category == DEROGATION and c.legal_review
    assert ids(c) == {"DER-ASSESS", "DER-REGISTER"}


def test_US04_derogation_is_rejected_when_the_system_profiles_people():
    c = classify(uc(annex_iii_area="5c_life_health_insurance_pricing", derogation_ground="preparatory_task",
                    profiling=True))
    assert c.category == HIGH_RISK and not c.legal_review
    assert any("cannot apply" in r for r in c.reasons)


# US-05 ------------------------------------------------------------------------------------------
def test_US05_chatbot_has_transparency_duty_from_august_2026():
    c = classify(uc(interacts_with_people=True, in_service_since="2026-09-01"))
    assert c.category == TRANSPARENCY
    (ob,) = c.obligations
    assert ob.id == "TR-INTERACT" and ob.due == date(2026, 8, 2)


def test_US05_marking_for_systems_already_in_service_is_due_december_2026():
    old = classify(uc(generates_synthetic_content=True, in_service_since="2026-03-01"))
    new = classify(uc(generates_synthetic_content=True, in_service_since="2026-09-01"))
    assert {o.id: o.due for o in old.obligations}["TR-MARKING"] == date(2026, 12, 2)
    assert {o.id: o.due for o in new.obligations}["TR-MARKING"] == date(2026, 8, 2)


def test_US05_nothing_flagged_is_minimal_with_no_obligations():
    c = classify(uc(profiling=True))
    assert c.category == MINIMAL and not c.obligations


# US-06 ------------------------------------------------------------------------------------------
def test_US06_deployer_gets_deployer_duties_only():
    dep = classify(uc(annex_iii_area="5b_creditworthiness", role="deployer"))
    prov = classify(uc(annex_iii_area="5b_creditworthiness", role="provider"))
    assert not any(i.startswith("HR-") for i in ids(dep)) and "DEP-FRIA" in ids(dep)
    assert all(i.startswith("HR-") for i in ids(prov))


def test_US06_deployer_of_generator_has_disclosure_not_marking():
    c = classify(uc(role="deployer", generates_synthetic_content=True, deepfake_published=True))
    assert ids(c) == {"TR-DEEPFAKE"}
    assert any("provider's duty" in r for r in c.reasons)


# US-07 ------------------------------------------------------------------------------------------
def test_US07_evidence_rows_are_checked(tmp_path):
    p, e, lit = write(tmp_path, [uc(id="A", interacts_with_people=True)],
                      [["A", "TR-INTERACT", "done", "", "x"], ["A", "HR-RISK", "done", "ref", "x"],
                       ["B", "TR-INTERACT", "done", "ref", "x"], ["A", "TR-INTERACT", "yes", "ref", "x"]])
    port = build(p, e, lit, AS_OF)
    text = " ".join(port.data_issues)
    assert "not done, partial or missing" in text
    assert "does not apply" in text and "unknown use case 'B'" in text


def test_US07_done_without_reference_counts_as_partial(tmp_path):
    p, e, lit = write(tmp_path, [uc(id="A", interacts_with_people=True)], [["A", "TR-INTERACT", "done", "", "x"]])
    port = build(p, e, lit, AS_OF)
    assert port.use_cases[0].obligations[0].evidence == "partial"
    assert any("no evidence reference" in x for x in port.data_issues)


# US-08 ------------------------------------------------------------------------------------------
def test_US08_overdue_obligation_turns_red_and_done_turns_green(tmp_path):
    p, e, lit = write(tmp_path, [uc(id="A", interacts_with_people=True), uc(id="B", interacts_with_people=True)],
                      [["B", "TR-INTERACT", "done", "UX-1", "x"]])
    port = build(p, e, lit, AS_OF)
    rag = {u.uc["id"]: u.rag for u in port.use_cases}
    assert rag == {"A": RED, "B": GREEN}
    assert port.use_cases[0].obligations[0].days_left == (date(2026, 8, 2) - AS_OF).days


def test_US08_open_future_obligation_is_amber(tmp_path):
    p, e, lit = write(tmp_path, [uc(id="A", annex_iii_area="5c_life_health_insurance_pricing")], [])
    port = build(p, e, lit, AS_OF)
    assert port.use_cases[0].rag == AMBER


# US-09 ------------------------------------------------------------------------------------------
def test_US09_literacy_below_target_is_flagged_and_high_risk_operators_named(tmp_path):
    p, e, lit = write(tmp_path, [uc(id="A")], [],
                      [["Underwriters", 100, 50, "yes", "role course"], ["Office", 100, 70, "no", "e-learning"],
                       ["Board", 10, 10, "no", "briefing"]])
    port = build(p, e, lit, AS_OF, literacy_target=0.8)
    d = " ".join(decisions(port))
    assert "2 role groups below the 80% internal target" in d and "Underwriters 50%" in d
    assert "Office" not in d.split("including")[1]


def test_US09_literacy_rows_are_validated(tmp_path):
    p, e, lit = write(tmp_path, [uc(id="A")], [], [["X", "ten", 3, "no", ""], ["Y", 5, 9, "no", ""]])
    port = build(p, e, lit, AS_OF)
    assert len(port.literacy) == 1 and port.literacy[0].completed == 5
    assert len(port.data_issues) == 2


# US-10 ------------------------------------------------------------------------------------------
def test_US10_pack_leads_with_decisions_and_never_claims_compliance(tmp_path):
    out = tmp_path / "out"
    rc = main(["report", "--portfolio", str(SAMPLE / "portfolio.json"), "--evidence", str(SAMPLE / "evidence.csv"),
               "--literacy", str(SAMPLE / "literacy.csv"), "--as-of", "2026-11-04", "--out", str(out)])
    assert rc == 0
    md = (out / "readiness-2026-11-04.md").read_text(encoding="utf-8")
    assert md.index("## Decisions for the executive committee") < md.index("## Portfolio at a glance")
    assert "not legal advice" in md and "2026/1744" in md
    assert "compliant" not in md.lower() and "certified" not in md.lower()
    data = json.loads((out / "readiness-2026-11-04.json").read_text(encoding="utf-8"))
    assert data["decisions"] and len(data["use_cases"]) == 11


# US-11 ------------------------------------------------------------------------------------------
def test_US11_sample_portfolio_shows_every_category_and_status():
    port = build(SAMPLE / "portfolio.json", SAMPLE / "evidence.csv", SAMPLE / "literacy.csv", AS_OF)
    cats = {u.uc["id"]: u.classification.category for u in port.use_cases}
    assert cats == {"UC01": HIGH_RISK, "UC02": MINIMAL, "UC03": MINIMAL, "UC04": TRANSPARENCY,
                    "UC05": PROHIBITED, "UC06": HIGH_RISK, "UC07": MINIMAL, "UC08": DEROGATION,
                    "UC09": HIGH_RISK, "UC10": TRANSPARENCY, "UC11": INSUFFICIENT}
    assert {u.rag for u in port.use_cases} == {RED, AMBER, GREEN}
    assert len(port.data_issues) == 2
    assert len(decisions(port)) == 6
    md = markdown(port, "Northwind Assurance (fictional)")
    assert "UC09" in md and "cannot apply" in md
    assert json.loads(as_json(port, "x"))["literacy"]
