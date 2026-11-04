# 2. Product requirements: AI Act readiness v0.1

Status: approved for MVP build, October 2026. Owner: product manager. Reviewers (planned): chief
data and AI officer, in-house counsel, chief compliance officer, tech lead.

## Problem statement

The executive committee is asked to fund and steer AI Act readiness without a view that joins
classification, obligations, evidence and deadlines for each AI use case. Late obligations are
found late, derogation claims go unchallenged, and literacy effort is spread evenly instead of
where risk is. (Evidence and hypotheses: [01-discovery.md](01-discovery.md).)

## Goal for v0.1

**One committee cycle run on the pack.** The AI governance lead produces it from three files in
under an hour; the first page lists the decisions the committee owns; every classification shows
the screening answers and the articles it rests on.

## Non-goals for v0.1

- Not legal advice and not a final classification: every category is a proposal for counsel.
- Not a GRC tool or system of record: the register, evidence log and training data stay where the
  organisation keeps them; this reads exports.
- No general-purpose AI model provider obligations (Chapter V): the sample insurer uses models,
  it does not place them on the market.
- No Annex I (product safety) route in v0.1 (US-14).
- No data-protection assessment: GDPR duties are named where they meet the Act, not assessed.
- No user interface beyond a generated pack.

## Core flow

1. The governance lead keeps three exports: the **portfolio** (one record per use case with the
   screening answers), the **evidence log** (use case, obligation, status, reference), and
   **literacy** coverage by role group.
2. `ai-act-readiness classify` prints each proposal with its reasons, for counsel to review.
3. `ai-act-readiness report --as-of <date>` writes the pack (Markdown for the paper, JSON for other
   tools): decisions first, then the portfolio table, literacy, detail per use case, data quality.
4. The committee decides; owners update evidence; the next cycle re-runs on the new exports.

## Requirements

| ID | Requirement | Priority | Story |
|---|---|---|---|
| R1 | No category on incomplete or unknown screening answers | Must | US-01 |
| R2 | Prohibited practices first, overriding every other result | Must | US-02 |
| R3 | Annex III uses classified high-risk, with provider and deployer obligations and the FRIA where required | Must | US-03 |
| R4 | Art. 6(3) derogation claims routed to legal review, and rejected where the system profiles people | Must | US-04 |
| R5 | Art. 50 transparency duties with the transitional date for systems already in service | Must | US-05 |
| R6 | Obligations filtered by role: provider, deployer, or both | Must | US-06 |
| R7 | Evidence validated: done needs a reference; inapplicable or unknown rows reported | Must | US-07 |
| R8 | Red / amber / green per use case from deadlines and evidence | Must | US-08 |
| R9 | AI literacy coverage per role group against an internal target, high-risk operators named | Should | US-09 |
| R10 | Pack opens with decisions, states its legal basis and that it is not legal advice, never says "compliant" | Must | US-10 |

Acceptance criteria per story: [../team/backlog.csv](../team/backlog.csv); each Done story is
proved by a named test ([../team/traceability.md](../team/traceability.md)). The rule table, with
articles and dates, is in [../legal-basis.md](../legal-basis.md).

## Status rules

| Status | Rule |
|---|---|
| Red | prohibited, or an obligation past its date without done evidence |
| Amber | open obligations not yet due, insufficient information, or a derogation in legal review |
| Green | every applicable obligation has done evidence with a reference |

## Success metrics

| Metric | Type | Target for the pilot | Source |
|---|---|---|---|
| Time to prepare the committee's AI Act status | North star | from the week-0 baseline (H1 expects over a day) to under 1 hour | governance lead's log |
| Classifications changed after counsel's review | Outcome (quality of the screening) | recorded for every use case; at least one in cycle 1 (H2) | counsel's review sheet |
| Use cases with complete screening | Adoption | 80% of live use cases by cycle 2 (H3) | `insufficient information` count |
| Committee decisions citing the pack | Outcome | at least one per cycle (H4) | minutes |
| Classifications reversed after the pack was used | Guardrail (trust) | zero without a recorded reason | decision log |

## Risks

| Risk | Mitigation |
|---|---|
| The pack is read as legal sign-off | "Proposal for legal review" on every page; no "compliant" wording (tested); counsel is a reviewer of this PRD |
| Owners answer the screening to get a lighter category | Derogations always go to counsel; profiling overrides the claim; sampled screening review in OPERATIONS.md |
| The law moves again | Rules in one versioned file with the date checked; US-15 re-runs the portfolio on a new version |
| Evidence marked done with nothing behind it | Done without a reference is downgraded and reported (US-07) |

## Release criteria for v0.1

All Must stories Done and proved in CI; the sample exercises every category and status; the scrub
check is clean; the README says the insurer is fictional and the data synthetic.
