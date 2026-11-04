# AI Act readiness: Northwind Assurance (fictional)

As of 2026-11-04. Rules: Regulation (EU) 2024/1689 (AI Act) as amended by Regulation (EU) 2026/1744 (Digital Omnibus on AI, in force 27 July 2026); dates checked 2026-11-04.

> Classification proposals for legal review, not legal advice. Every line below shows the screening answers and articles it rests on, so it can be challenged.

## Decisions for the executive committee

1. **Stop or redesign** UC05 (Call-centre voice sentiment for agent coaching): the screening matches a prohibited practice, applicable since 2 February 2025.
2. **Close overdue obligations now:** UC04 TR-INTERACT (Art. 50(1)).
3. **Ask counsel to confirm the Art. 6(3) derogation** for UC08; plan as high-risk until it is confirmed.
4. **Fund the high-risk programme:** 3 systems, 31 of 34 obligations open, first due 2 December 2027 (13 months left).
5. **Complete the screening** for UC11 before it progresses: no category is proposed on missing answers.
6. **AI literacy:** 3 role groups below the 80% internal target, including staff who operate high-risk systems (Life and health underwriters 67%, Recruiters and hiring managers 32%).

## Portfolio at a glance

11 use cases: 1 prohibited, 3 high-risk, 1 not high-risk (Art. 6(3) claimed, legal review), 2 transparency obligations, 3 minimal risk, 1 insufficient information. Status: 2 red, 5 amber, 4 green.

| Use case | Unit | Role | Proposed category | Status | Open obligations | Next due |
|---|---|---|---|---|---|---|
| UC04 Customer service assistant | Customer Service | provider and deployer | transparency obligations | RED | 2 of 2 | 2026-08-02 |
| UC05 Call-centre voice sentiment for agent coaching | Customer Service | deployer | prohibited | RED | 1 of 1 | 2025-02-02 |
| UC01 Life and health underwriting score | Underwriting | provider and deployer | high-risk | AMBER | 12 of 15 | 2027-12-02 |
| UC06 CV screening for graduate hiring | People and Culture | deployer | high-risk | AMBER | 4 of 4 | 2027-12-02 |
| UC08 Health tariff data-quality checker | Pricing | provider and deployer | not high-risk (Art. 6(3) claimed, legal review) | AMBER | 1 of 2 | 2027-12-02 |
| UC09 Health cover premium personalisation | Pricing | provider and deployer | high-risk | AMBER | 15 of 15 | 2027-12-02 |
| UC11 Broker email summariser | Commercial Lines | deployer | insufficient information | AMBER | 0 of 0 | - |
| UC02 Motor claims triage | Claims | provider and deployer | minimal risk | GREEN | 0 of 0 | - |
| UC03 Claims fraud signals | Claims | provider and deployer | minimal risk | GREEN | 0 of 0 | - |
| UC07 Staff productivity assistant | Group IT | deployer | minimal risk | GREEN | 0 of 0 | - |
| UC10 Campaign image generation | Marketing | deployer | transparency obligations | GREEN | 0 of 1 | - |

## AI literacy (Art. 4)

Since the 2026 amendment, Art. 4 asks providers and deployers to take measures supporting AI literacy and does not require a guaranteed level. The coverage target (--literacy-target) is the organisation's own policy choice, not a legal threshold.

| Role group | In scope | Completed | Coverage | Operates high-risk AI | Measures |
|---|---|---|---|---|---|
| Executive Committee and board | 14 | 14 | 100% | no | Half-day briefing on AI risk and the AI Act |
| Life and health underwriters | 180 | 121 | 67% (below target) | yes | Role course: the score's limits and when to override it |
| Pricing actuaries | 40 | 38 | 95% | yes | Role course plus model-risk refresher |
| Recruiters and hiring managers | 60 | 19 | 32% (below target) | yes | Vendor tool training; bias module not yet run |
| Claims handlers | 520 | 463 | 89% | no | Triage and fraud-signal course |
| Customer service agents | 310 | 288 | 93% | no | Assistant course: what it may and may not answer |
| IT and data teams | 220 | 205 | 93% | no | Engineering course on the internal AI standards |
| All other office staff | 1900 | 1140 | 60% (below target) | no | E-learning: using the productivity assistant safely |
| **All** | 3244 | 2288 | 71% | | |

## Use case detail

### UC01 Life and health underwriting score: high-risk (AMBER)

Scores applicants for life and health cover and proposes a premium band; underwriters confirm.

- Use falls under Annex III, point 5(c).
- As a deployer under point 5(b) or 5(c), it needs a fundamental rights impact assessment before use (Art. 27).

**Next:** Fund and plan 12 open obligations, first due 2027-12-02.

| Obligation | Article | Due | Evidence | Days left |
|---|---|---|---|---|
| HR-RISK Risk management system | Art. 9 | 2027-12-02 | partial (RM-UW-2026-03: draft risk register) | 393 |
| HR-DATA Data and data governance | Art. 10 | 2027-12-02 | partial (DG-UW-07: data lineage done; bias testing open) | 393 |
| HR-DOC Technical documentation | Art. 11, Annex IV | 2027-12-02 | missing | 393 |
| HR-LOG Automatic logging | Art. 12 | 2027-12-02 | done (LOG-UW-01) | - |
| HR-INFO Instructions for use for deployers | Art. 13 | 2027-12-02 | missing | 393 |
| HR-OVERSIGHT Human oversight by design | Art. 14 | 2027-12-02 | done (UW-SOP-12: underwriter confirms every band) | - |
| HR-ROBUST Accuracy, robustness and cybersecurity | Art. 15 | 2027-12-02 | partial (VAL-UW-2025: model validation; no drift monitoring) | 393 |
| HR-QMS Quality management system | Art. 17 | 2027-12-02 | missing | 393 |
| HR-CONFORMITY Conformity assessment and EU declaration | Art. 43, 47 | 2027-12-02 | missing | 393 |
| HR-REGISTER Registration in the EU database | Art. 49(1) | 2027-12-02 | missing | 393 |
| HR-PMM Post-market monitoring | Art. 72 | 2027-12-02 | missing | 393 |
| DEP-USE Use per instructions; assign competent human oversight | Art. 26(1)-(2) | 2027-12-02 | done (UW-SOP-12) | - |
| DEP-MONITOR Monitor operation; keep logs at least six months | Art. 26(5)-(6) | 2027-12-02 | partial (LOG-UW-01: retention 90 days) | 393 |
| DEP-PERSONS Inform people subject to decisions; explanation on request | Art. 26(11), 86 | 2027-12-02 | missing | 393 |
| DEP-FRIA Fundamental rights impact assessment before first use | Art. 27 | 2027-12-02 | missing | 393 |

### UC02 Motor claims triage: minimal risk (GREEN)

Routes new motor claims to fast-track or specialist queues by complexity.

- No prohibited practice and no Annex III use in the screening answers.

### UC03 Claims fraud signals: minimal risk (GREEN)

Flags claims with fraud indicators for an investigator to review.

- No prohibited practice and no Annex III use in the screening answers.
- The system profiles people, but outside an Annex III use profiling alone does not make it high-risk under the AI Act (data-protection rules still apply).

### UC04 Customer service assistant: transparency obligations (RED)

A chat assistant on the website and app, built on a general-purpose model, answering policy questions.

- No prohibited practice and no Annex III use in the screening answers.
- The system interacts directly with people.
- The system generates synthetic content.

**Next:** Close overdue obligations now: TR-INTERACT. Fund and plan 1 open obligation, first due 2026-12-02.

| Obligation | Article | Due | Evidence | Days left |
|---|---|---|---|---|
| TR-INTERACT Tell people they are interacting with an AI system | Art. 50(1) | 2026-08-02 | missing | -94 (overdue) |
| TR-MARKING Machine-readable marking of synthetic output | Art. 50(2); Art. 111(4) | 2026-12-02 | partial (ARCH-CS-04: metadata on exported transcripts only) | 28 |

### UC05 Call-centre voice sentiment for agent coaching: prohibited (RED)

Infers agents' emotional state from call audio to target coaching.

- Emotion recognition at the workplace is prohibited (Art. 5(1)(f)), unless for medical or safety reasons, which the screening does not record.

**Next:** Stop the use, or redesign it so the prohibited element is removed; record the decision.

| Obligation | Article | Due | Evidence | Days left |
|---|---|---|---|---|
| PROHIB Stop or redesign: prohibited practice | Art. 5 | 2025-02-02 | missing | -640 (overdue) |

### UC06 CV screening for graduate hiring: high-risk (AMBER)

A vendor tool that ranks graduate applications before recruiter review.

- Use falls under Annex III, point 4(a).

**Next:** Fund and plan 4 open obligations, first due 2027-12-02.

| Obligation | Article | Due | Evidence | Days left |
|---|---|---|---|---|
| DEP-USE Use per instructions; assign competent human oversight | Art. 26(1)-(2) | 2027-12-02 | partial (Vendor instructions received; oversight owner not named) | 393 |
| DEP-MONITOR Monitor operation; keep logs at least six months | Art. 26(5)-(6) | 2027-12-02 | missing | 393 |
| DEP-WORKERS Inform workers' representatives and affected workers | Art. 26(7) | 2027-12-02 | missing | 393 |
| DEP-PERSONS Inform people subject to decisions; explanation on request | Art. 26(11), 86 | 2027-12-02 | missing | 393 |

### UC07 Staff productivity assistant: minimal risk (GREEN)

A licensed general-purpose assistant for drafting and summarising, used by office staff.

- No prohibited practice and no Annex III use in the screening answers.

### UC08 Health tariff data-quality checker: not high-risk (Art. 6(3) claimed, legal review) (AMBER)

Checks tariff tables for format and range errors before actuaries set health prices; makes no decision about any person.

- Use falls under Annex III, point 5(c); the owner claims Art. 6(3)(a) ('narrow_procedural_task') and no profiling. Legal review must confirm the derogation before the system is treated as not high-risk.

**Next:** Legal review of the Art. 6(3) derogation; until confirmed, plan as high-risk. Fund and plan 1 open obligation, first due 2027-12-02.

| Obligation | Article | Due | Evidence | Days left |
|---|---|---|---|---|
| DER-ASSESS Document the Art. 6(3) assessment before use | Art. 6(4) | 2027-12-02 | done (LEGAL-AIA-08: assessment memo) | - |
| DER-REGISTER Register the system as not high-risk | Art. 49(2) | 2027-12-02 | missing | 393 |

### UC09 Health cover premium personalisation: high-risk (AMBER)

Adjusts health premiums from customer behaviour data; the owner argues it only prepares the actuary's decision.

- Use falls under Annex III, point 5(c). The Art. 6(3) derogation claimed ('preparatory_task') cannot apply because the system profiles natural persons (Art. 6(3), last subparagraph).
- As a deployer under point 5(b) or 5(c), it needs a fundamental rights impact assessment before use (Art. 27).

**Next:** Fund and plan 15 open obligations, first due 2027-12-02.

| Obligation | Article | Due | Evidence | Days left |
|---|---|---|---|---|
| HR-RISK Risk management system | Art. 9 | 2027-12-02 | missing | 393 |
| HR-DATA Data and data governance | Art. 10 | 2027-12-02 | missing | 393 |
| HR-DOC Technical documentation | Art. 11, Annex IV | 2027-12-02 | missing | 393 |
| HR-LOG Automatic logging | Art. 12 | 2027-12-02 | missing | 393 |
| HR-INFO Instructions for use for deployers | Art. 13 | 2027-12-02 | missing | 393 |
| HR-OVERSIGHT Human oversight by design | Art. 14 | 2027-12-02 | partial (Actuary sign-off on monthly batch) | 393 |
| HR-ROBUST Accuracy, robustness and cybersecurity | Art. 15 | 2027-12-02 | missing | 393 |
| HR-QMS Quality management system | Art. 17 | 2027-12-02 | missing | 393 |
| HR-CONFORMITY Conformity assessment and EU declaration | Art. 43, 47 | 2027-12-02 | missing | 393 |
| HR-REGISTER Registration in the EU database | Art. 49(1) | 2027-12-02 | missing | 393 |
| HR-PMM Post-market monitoring | Art. 72 | 2027-12-02 | missing | 393 |
| DEP-USE Use per instructions; assign competent human oversight | Art. 26(1)-(2) | 2027-12-02 | missing | 393 |
| DEP-MONITOR Monitor operation; keep logs at least six months | Art. 26(5)-(6) | 2027-12-02 | missing | 393 |
| DEP-PERSONS Inform people subject to decisions; explanation on request | Art. 26(11), 86 | 2027-12-02 | missing | 393 |
| DEP-FRIA Fundamental rights impact assessment before first use | Art. 27 | 2027-12-02 | missing | 393 |

### UC10 Campaign image generation: transparency obligations (GREEN)

A licensed image generator producing realistic campaign images of people who do not exist.

- No prohibited practice and no Annex III use in the screening answers.
- The system generates synthetic content.
- The system publishes deep fakes or AI-generated text.
- Machine-readable marking (Art. 50(2)) is the provider's duty; as a deployer, check that the vendor provides it.

| Obligation | Article | Due | Evidence | Days left |
|---|---|---|---|---|
| TR-DEEPFAKE Disclose deep fakes and AI-generated published text | Art. 50(4) | 2026-08-02 | done (MKT-POL-22: AI-generated label on every image) | - |

### UC11 Broker email summariser: insufficient information (AMBER)

Proposed: summarise broker emails and draft replies.

- Screening incomplete: profiling, interacts_with_people, generates_synthetic_content, deepfake_published, emotion_recognition. No category is proposed until every question is answered.

**Next:** Complete the screening questions before any classification is proposed.

## Data quality

- evidence.csv row 29: marked done with no evidence reference; treated as partial
- evidence.csv: UC03 has evidence for HR-RISK, which does not apply to its proposed category; ignored (check the screening or the evidence row)

## Basis

Dates and article references are a reading of the consolidated text for a portfolio screening tool. They are not legal advice; confirm against EUR-Lex and with legal counsel.
