# Operations: sample operating model for the pilot

Designed for a pilot; operated so far as a prototype on synthetic data. Thresholds below are the
plan, not measurements.

## 1. Release gate (ticked before each release to the pilot)

- [ ] CI green: tests, `tools/trace.py` (every Done story has a test), scrub check
- [ ] Sample portfolio still shows every category and status (`test_US11_...`)
- [ ] Any change to `rules.json` reviewed by counsel, with the date checked updated and a line in
      [docs/legal-basis.md](docs/legal-basis.md) and the CHANGELOG
- [ ] Previous release tag kept; the governance lead knows how to re-run it
- [ ] Governance lead and counsel told what changed, in two lines

A release that fails any line does not go out.

## 2. Rollout

One committee, 8-15 use cases, two cycles. Success metric and decision rules are fixed in
[03-roadmap-and-pilot.md](docs/product/03-roadmap-and-pilot.md) before launch.

## 3. Monitoring

| Signal | Source | Frequency | Alert when |
|---|---|---|---|
| Screening completeness | `insufficient information` count | per cycle | over 20% of live use cases by cycle 2 |
| Counsel's changes to proposals | counsel's review sheet | per cycle | over a third of reasons rewritten (fix the screening, not the rules) |
| Overdue obligations | pack, red count | per cycle | any red not on the committee agenda |
| Data-quality findings | pack, data-quality section | per cycle | done-without-reference rows after cycle 1 |
| Pack preparation time | governance lead's log | per cycle | over 1 hour |
| Rules freshness | `checked` date in `rules.json` | monthly | older than 3 months, or a new act or guideline published |

Format of the cycle log: [ops/sample-monitoring-log.csv](ops/sample-monitoring-log.csv) (labelled sample row).

## 4. Feedback into evaluations

Every confirmed misclassification or wrong date becomes a must-pass case in
[evals/EVALS.md](evals/EVALS.md) and a test named after its story **before** the fix ships.

## 5. Change and drift

The regression set re-runs on any change to `rules.json`, the status rules or an input format,
and when the Commission publishes guidance on high-risk classification (due 2027) or the Act is
amended again. A must-pass case that regresses means rollback to the previous tag unless fixed the
same day.

## 6. Incident runbook

| Incident | Detected by | Contain | Tell | Follow-up |
|---|---|---|---|---|
| A use case shown as minimal or green that counsel later finds high-risk | counsel review, audit | re-run on corrected screening; mark the pack superseded | committee chair, counsel | new eval case; check whether other use cases share the screening pattern |
| Wrong date or article in `rules.json` | counsel, monitoring of the official journal | revert to the previous tag; re-issue the pack | governance lead, counsel | correct the rule with source; CHANGELOG line |
| Pack read as legal sign-off | minutes, stakeholder feedback | written correction to the committee | sponsor, counsel | strengthen the header wording; review D1 and D9 |
| Sensitive evidence references circulated outside the committee | distribution check | recall the pack; share the JSON only with the GRC owner | sponsor, information-security | restrict distribution list in the release gate |

## 7. Ownership and retirement

Owner: AI governance lead; backup: product manager; counsel owns `rules.json`. Review every three
months. Retire when the organisation's GRC tool covers classification, obligations and evidence
with the same transparency, or when the pack is not used for two consecutive cycles.
