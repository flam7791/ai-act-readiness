# Team brief: AI Act readiness

One page for the people who take this from v0.1 to a running pilot. Read this first.

## Mission

Give the executive committee a readiness view it can act on, and counsel one it can check, so
that late obligations are found while there is still time to fund them.

## Where we are

v0.1 works end to end on a fictional insurer's portfolio: three files in, an executive pack out,
every classification showing its reasons and articles ([sample pack](../sample-report.md)).
Eleven stories are Done and proved by tests in CI. What we do not know yet is whether counsel
accepts the proposals as a starting point, and whether owners will answer the screening. Finding
that out is the job of the next two committee cycles.

## The next six weeks

1. Sprint 3: changes since the last review (US-12) and the owner questionnaire (US-13).
2. Pilot cycle 1 run on the pack, counsel's agree / change recorded for every use case.
3. Every confirmed problem from the pilot is a backlog item with a failing test.

## Constraints not up for debate in this phase

- **The tool proposes; counsel classifies** (D1). No feature marks a classification as final.
- **Never "compliant"** (D9). Green means evidence with a reference for every listed obligation.
- **Rules change only with counsel's review** (D5): `rules.json` changes need a PR reviewed by counsel.
- **No personal data in the evidence log**: references point to documents, not people.

## Who does what (RACI)

| Activity | Governance lead | Counsel | Product manager | Tech lead | Use-case owners | Committee |
|---|---|---|---|---|---|---|
| Screening answers per use case | A | C | I | | R | |
| Classification review | R | A | I | | C | I |
| Rules file changes | C | A | R | R | | |
| Evidence updates | A | | | | R | |
| Pack preparation | R/A | C | C | C | | I |
| Decisions (stop, fund, accept risk) | R | C | | | C | A |
| Product scope and priorities | C | C | A/R | C | | |

## Links

[Backlog](backlog.csv) · [traceability](traceability.md) · [working agreement](working-agreement.md) ·
[PRD](../product/02-prd.md) · [legal basis](../legal-basis.md) · [OPERATIONS](../../OPERATIONS.md)
