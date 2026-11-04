# Evaluation cases and run log

The product makes no model calls, so its evaluations are acceptance cases run as tests on every
push. All cases are **must-pass** and form the **regression set**: they run on every release and
whenever `rules.json`, a status rule or an input format changes.

| # | Case | Kind | Pass condition | Test |
|---|---|---|---|---|
| E1 | Sample insurer, 11 use cases | happy path | every category and status appears; six decisions; two data-quality findings | `test_US11_sample_portfolio_shows_every_category_and_status` |
| E2 | Pack written from the sample | happy path | decisions before tables; basis and "not legal advice" stated; MD and JSON written | `test_US10_pack_leads_with_decisions_and_never_claims_compliance` |
| E3 | Recruitment tool bought from a vendor | not in the sample's shape | deployer duties and worker information, no FRIA, no provider duties | `test_US03_recruitment_is_high_risk...`, `test_US06_deployer_gets_deployer_duties_only` |
| E4 | Owner claims a derogation for a profiling system | hostile input (gaming the category) | claim rejected with the reason; stays high-risk | `test_US04_derogation_is_rejected_when_the_system_profiles_people` |
| E5 | Evidence marked done with no reference, or for an obligation that does not apply | hostile input (false assurance) | downgraded to partial or ignored, and reported | `test_US07_*` |
| E6 | Use case with half the screening answered | nothing to go on | insufficient information, missing fields listed, no obligations | `test_US01_missing_answers_give_insufficient_not_minimal` |
| E7 | Unknown practice code, Annex III area or role | nothing to go on | insufficient information, nothing guessed | `test_US01_unknown_codes_and_roles_are_not_guessed` |
| E8 | Pack wording | boundary (the tool does not certify) | "compliant" and "certified" never appear | `test_US10_pack_leads_with_decisions_and_never_claims_compliance` |
| E9 | Workplace emotion recognition also flagged as customer-facing | acceptance | prohibited wins; only the Stop obligation | `test_US02_workplace_emotion_recognition_is_prohibited` |
| E10 | Generative assistant in service before and after 2 August 2026 | acceptance (dates) | marking due 2 Dec 2026 and 2 Aug 2026 respectively | `test_US05_marking_for_systems_already_in_service...` |
| E11 | Chatbot with no disclosure evidence, as of November 2026 | acceptance (status) | red, overdue, days counted from --as-of | `test_US08_overdue_obligation_turns_red_and_done_turns_green` |
| E12 | Literacy below the internal target | acceptance | groups below target listed; high-risk operators named; target labelled a policy choice | `test_US09_*` |

## Run log

| Date | Version | Result | Change |
|---|---|---|---|
| 2026-11-04 | 0.1.0 | 21/21 tests, 11/11 Done stories traced, Python 3.12 locally | first build |
