"""Classify one AI use case under the AI Act and list the obligations that follow.

The output is a *classification proposal for legal review*: every result carries the articles
and the screening answers it rests on, so a lawyer can check the reasoning rather than trust it.
A missing screening answer gives INSUFFICIENT, never a silent "minimal risk".
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import date
from importlib import resources

PROHIBITED = "prohibited"
HIGH_RISK = "high-risk"
DEROGATION = "not high-risk (Art. 6(3) claimed, legal review)"
TRANSPARENCY = "transparency obligations"
MINIMAL = "minimal risk"
INSUFFICIENT = "insufficient information"

ROLES = {"provider", "deployer", "provider_and_deployer"}
SCREENING_FIELDS = [
    "role", "prohibited_practice", "annex_iii_area", "profiling",
    "interacts_with_people", "generates_synthetic_content", "deepfake_published",
    "emotion_recognition",
]


def load_rules() -> dict:
    return json.loads(resources.files("ai_act_readiness").joinpath("rules.json").read_text(encoding="utf-8"))


@dataclass
class Obligation:
    id: str
    title: str
    ref: str
    due: date


@dataclass
class Classification:
    use_case_id: str
    category: str
    reasons: list[str] = field(default_factory=list)
    obligations: list[Obligation] = field(default_factory=list)
    missing: list[str] = field(default_factory=list)
    legal_review: bool = False


def _role_matches(ob_role: str, uc_role: str) -> bool:
    if ob_role == "any":
        return True
    return uc_role == ob_role or uc_role == "provider_and_deployer"


def classify(uc: dict, rules: dict | None = None) -> Classification:
    rules = rules or load_rules()
    uid = uc.get("id", "?")

    missing = [f for f in SCREENING_FIELDS if f not in uc]
    if uc.get("role") is not None and uc.get("role") not in ROLES:
        missing.append("role (must be provider, deployer or provider_and_deployer)")
    if missing:
        return Classification(uid, INSUFFICIENT, [f"Screening incomplete: {', '.join(missing)}. "
                                                  "No category is proposed until every question is answered."],
                              missing=missing)

    role = uc["role"]
    reasons: list[str] = []
    tags: set[str] = set()
    legal_review = False

    practice = uc["prohibited_practice"]
    area = uc["annex_iii_area"]
    if practice:
        ref = rules["prohibited_practices"].get(practice)
        if ref is None:
            return Classification(uid, INSUFFICIENT, [f"Unknown prohibited-practice code '{practice}'."],
                                  missing=["prohibited_practice"])
        category = PROHIBITED
        tags.add("prohibited")
        reasons.append(f"Screening answer '{practice}' matches a prohibited practice ({ref}).")
    elif area:
        ref = rules["annex_iii_areas"].get(area)
        if ref is None:
            return Classification(uid, INSUFFICIENT, [f"Unknown Annex III area '{area}'."], missing=["annex_iii_area"])
        ground = uc.get("derogation_ground")
        if ground and uc["profiling"]:
            category = HIGH_RISK
            reasons.append(f"Use falls under {ref}. The Art. 6(3) derogation claimed ('{ground}') cannot apply "
                           "because the system profiles natural persons (Art. 6(3), last subparagraph).")
        elif ground:
            gref = rules["derogation_grounds"].get(ground)
            if gref is None:
                return Classification(uid, INSUFFICIENT, [f"Unknown derogation ground '{ground}'."],
                                      missing=["derogation_ground"])
            category = DEROGATION
            legal_review = True
            tags.add("derogation")
            reasons.append(f"Use falls under {ref}; the owner claims {gref} ('{ground}') and no profiling. "
                           "Legal review must confirm the derogation before the system is treated as not high-risk.")
        else:
            category = HIGH_RISK
            reasons.append(f"Use falls under {ref}.")
        if category == HIGH_RISK:
            tags.add("high_risk")
            if area in rules["fria_areas"] and role != "provider":
                tags.add("high_risk_fria")
                reasons.append("As a deployer under point 5(b) or 5(c), it needs a fundamental rights impact assessment before use (Art. 27).")
            if area.startswith("4"):
                tags.add("high_risk_workplace")
    else:
        category = MINIMAL
        reasons.append("No prohibited practice and no Annex III use in the screening answers.")
        if uc["profiling"]:
            reasons.append("The system profiles people, but outside an Annex III use profiling alone does not make it "
                           "high-risk under the AI Act (data-protection rules still apply).")

    if category != PROHIBITED:
        emo = uc["emotion_recognition"]
        if emo == "workplace":
            category, tags = PROHIBITED, {"prohibited"}
            reasons = [f"Emotion recognition at the workplace is prohibited "
                       f"({rules['prohibited_practices']['emotion_recognition_workplace_or_education']}), "
                       "unless for medical or safety reasons, which the screening does not record."]
        else:
            for flag, label in [("interacts_with_people", "interacts directly with people"),
                                ("generates_synthetic_content", "generates synthetic content"),
                                ("deepfake_published", "publishes deep fakes or AI-generated text")]:
                if uc[flag]:
                    tags.add(flag)
                    reasons.append(f"The system {label}.")
            if uc["generates_synthetic_content"] and role == "deployer":
                reasons.append("Machine-readable marking (Art. 50(2)) is the provider's duty; as a deployer, "
                               "check that the vendor provides it.")
            if emo == "other":
                tags.add("emotion_recognition_permitted")
                reasons.append("The system recognises emotions outside the workplace and education.")
            if category == MINIMAL and tags & {"interacts_with_people", "generates_synthetic_content",
                                               "deepfake_published", "emotion_recognition_permitted"}:
                category = TRANSPARENCY

    in_service = uc.get("in_service_since")
    obligations = []
    for ob in rules["obligations"]:
        if ob["applies_to"] not in tags or not _role_matches(ob["role"], role):
            continue
        due, ref = ob["due"], ob["ref"]
        alt = ob.get("due_if_in_service_before")
        if alt and in_service and in_service < alt["date"]:
            due, ref = alt["due"], f"{ref}; {alt['ref']}"
        obligations.append(Obligation(ob["id"], ob["title"], ref, date.fromisoformat(due)))

    return Classification(uid, category, reasons, obligations, legal_review=legal_review)
