# Legal basis used by the rules

Basis: Regulation (EU) 2024/1689 (AI Act) as amended by Regulation (EU) 2026/1744 (Digital Omnibus on AI, in force 27 July 2026). Dates checked 2026-11-04.

> Dates and article references are a reading of the consolidated text for a portfolio screening tool. They are not legal advice; confirm against EUR-Lex and with legal counsel.

## Timeline that matters to the sample portfolio

| Date | What applies | Source |
|---|---|---|
| 2 February 2025 | Prohibited practices (Art. 5); AI literacy (Art. 4) | Regulation (EU) 2024/1689, Art. 113 |
| 2 August 2025 | General-purpose AI model obligations; penalties | Art. 113 |
| 2 August 2026 | General application, including Art. 50 transparency duties | Art. 113 |
| 2 December 2026 | Art. 50(2) marking for generative systems already in service before 2 August 2026 | Art. 111(4) as amended by Regulation (EU) 2026/1744 |
| 2 December 2027 | High-risk requirements for Annex III uses (Chapter III, Sections 1-3), moved from 2 August 2026 | Regulation (EU) 2026/1744 |
| 2 August 2028 | High-risk requirements for Annex I products, moved from 2 August 2027 (not modelled in v0.1) | Regulation (EU) 2026/1744 |

The 2026 amendment also softened Art. 4: providers and deployers "take measures to support" AI literacy, with no guaranteed level. The pack therefore treats the coverage target as an internal policy setting.

## Readings counsel should confirm

- Every obligation attached to a high-risk classification, including registration (Art. 49),
  conformity assessment (Art. 43) and post-market monitoring (Art. 72), is dated 2 December 2027,
  on the reading that these duties bite on Annex III systems once the high-risk rules apply.
- The Art. 6(4) assessment and Art. 49(2) registration for a derogation claim carry the same date.
- The two prohibitions added by the 2026 amendment (applicable from 2 December 2026) are not yet
  screening codes; none of the sample use cases is near them.

## Screening codes

| Code | Meaning | Reference |
|---|---|---|
| `manipulative_techniques` | prohibited practice | Art. 5(1)(a) |
| `exploiting_vulnerabilities` | prohibited practice | Art. 5(1)(b) |
| `social_scoring` | prohibited practice | Art. 5(1)(c) |
| `crime_prediction_by_profiling` | prohibited practice | Art. 5(1)(d) |
| `untargeted_facial_scraping` | prohibited practice | Art. 5(1)(e) |
| `emotion_recognition_workplace_or_education` | prohibited practice | Art. 5(1)(f) |
| `biometric_categorisation_sensitive` | prohibited practice | Art. 5(1)(g) |
| `realtime_remote_biometric_identification_public` | prohibited practice | Art. 5(1)(h) |
| `1_biometrics` | Annex III use | Annex III, point 1 |
| `2_critical_infrastructure` | Annex III use | Annex III, point 2 |
| `3_education` | Annex III use | Annex III, point 3 |
| `4a_recruitment_selection` | Annex III use | Annex III, point 4(a) |
| `4b_work_decisions_monitoring` | Annex III use | Annex III, point 4(b) |
| `5a_public_benefits` | Annex III use | Annex III, point 5(a) |
| `5b_creditworthiness` | Annex III use | Annex III, point 5(b) |
| `5c_life_health_insurance_pricing` | Annex III use | Annex III, point 5(c) |
| `5d_emergency_dispatch` | Annex III use | Annex III, point 5(d) |
| `narrow_procedural_task` | derogation ground claimed | Art. 6(3)(a) |
| `improves_completed_human_activity` | derogation ground claimed | Art. 6(3)(b) |
| `detects_patterns_without_replacing_review` | derogation ground claimed | Art. 6(3)(c) |
| `preparatory_task` | derogation ground claimed | Art. 6(3)(d) |

## Obligations

| Id | Obligation | Reference | Applies when | Role | Due |
|---|---|---|---|---|---|
| PROHIB | Stop or redesign: prohibited practice | Art. 5 | `prohibited` | any | 2025-02-02 |
| HR-RISK | Risk management system | Art. 9 | `high_risk` | provider | 2027-12-02 |
| HR-DATA | Data and data governance | Art. 10 | `high_risk` | provider | 2027-12-02 |
| HR-DOC | Technical documentation | Art. 11, Annex IV | `high_risk` | provider | 2027-12-02 |
| HR-LOG | Automatic logging | Art. 12 | `high_risk` | provider | 2027-12-02 |
| HR-INFO | Instructions for use for deployers | Art. 13 | `high_risk` | provider | 2027-12-02 |
| HR-OVERSIGHT | Human oversight by design | Art. 14 | `high_risk` | provider | 2027-12-02 |
| HR-ROBUST | Accuracy, robustness and cybersecurity | Art. 15 | `high_risk` | provider | 2027-12-02 |
| HR-QMS | Quality management system | Art. 17 | `high_risk` | provider | 2027-12-02 |
| HR-CONFORMITY | Conformity assessment and EU declaration | Art. 43, 47 | `high_risk` | provider | 2027-12-02 |
| HR-REGISTER | Registration in the EU database | Art. 49(1) | `high_risk` | provider | 2027-12-02 |
| HR-PMM | Post-market monitoring | Art. 72 | `high_risk` | provider | 2027-12-02 |
| DEP-USE | Use per instructions; assign competent human oversight | Art. 26(1)-(2) | `high_risk` | deployer | 2027-12-02 |
| DEP-MONITOR | Monitor operation; keep logs at least six months | Art. 26(5)-(6) | `high_risk` | deployer | 2027-12-02 |
| DEP-WORKERS | Inform workers' representatives and affected workers | Art. 26(7) | `high_risk_workplace` | deployer | 2027-12-02 |
| DEP-PERSONS | Inform people subject to decisions; explanation on request | Art. 26(11), 86 | `high_risk` | deployer | 2027-12-02 |
| DEP-FRIA | Fundamental rights impact assessment before first use | Art. 27 | `high_risk_fria` | deployer | 2027-12-02 |
| DER-ASSESS | Document the Art. 6(3) assessment before use | Art. 6(4) | `derogation` | provider | 2027-12-02 |
| DER-REGISTER | Register the system as not high-risk | Art. 49(2) | `derogation` | provider | 2027-12-02 |
| TR-INTERACT | Tell people they are interacting with an AI system | Art. 50(1) | `interacts_with_people` | provider | 2026-08-02 |
| TR-MARKING | Machine-readable marking of synthetic output | Art. 50(2) | `generates_synthetic_content` | provider | 2026-08-02; 2026-12-02 if in service before 2026-08-02 |
| TR-EMOTION | Inform people exposed to emotion recognition or biometric categorisation | Art. 50(3) | `emotion_recognition_permitted` | deployer | 2026-08-02 |
| TR-DEEPFAKE | Disclose deep fakes and AI-generated published text | Art. 50(4) | `deepfake_published` | deployer | 2026-08-02 |
| LIT | Measures to support AI literacy of staff and others operating AI on the organisation's behalf | Art. 4 (as amended) | always | any | 2025-02-02 |

## Sources checked

- Regulation (EU) 2024/1689 (AI Act), Official Journal, 12 July 2024.
- Regulation (EU) 2026/1744 amending Regulation (EU) 2024/1689 (Digital Omnibus on AI), Official Journal, 24 July 2026; in force 27 July 2026.
- Secondary summaries of the amended timeline (Future of Privacy Forum; ActuIA), read 4 November 2026. Confirm against EUR-Lex before relying on any date.
