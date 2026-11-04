# Working agreement

## Definition of Ready (a story can enter a sprint when)

- It has a user, a need and a reason ("As a ... I want ... so that ...").
- Its acceptance criteria are observable: a reviewer can check each one without asking the author.
- Dependencies outside the team are resolved or named with an owner and a date (for example,
  counsel's sign-off on a rules change).
- It is estimated, and it fits in one sprint (8 points or fewer; split otherwise).

## Definition of Done (a story is Done when)

- Every acceptance criterion is met and the PM has accepted it at the demo.
- At least one test named `test_<STORY>_...` proves it; `python tools/trace.py` passes. CI enforces this.
- CI is green: tests, traceability, scrub check.
- Any changed rule, date or status definition is updated in the PRD, the legal basis or the decision log in the same PR.
- The CHANGELOG has a line for anything a user would notice.

## Rituals

| Ritual | When | Who | Output |
|---|---|---|---|
| Sprint planning | Monday, week 1, 60 min | Team | Sprint goal (one sentence) and committed stories |
| Stand-up | Daily, 15 min | Team | Blockers named with an owner |
| Backlog refinement | Wednesday, week 2, 45 min | PM, tech lead, one engineer | Next sprint's stories Ready |
| Demo | Friday, week 2, 30 min | Team plus the AI governance lead and counsel (the real users) | Accepted / not accepted per story; feedback as new backlog items |
| Retrospective | Friday, week 2, 30 min | Team | One change to try next sprint |

## Pull requests

- Small: one story or less per PR. The title starts with the story id (`US-10: ...`).
- One reviewer from the team; in-house counsel as well if `rules.json` changes.
- The PR template's checklist is the Definition of Done.

## Disagreements

Decisions about *what* and *in which order* are the PM's; about *how* the tech lead's. If either
is challenged, write the disagreement as a decision-log entry with both options; the accountable
person decides within two working days and the entry records why.
