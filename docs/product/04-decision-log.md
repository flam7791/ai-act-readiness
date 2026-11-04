# 4. Decision log

Decisions that someone could reasonably question later, with the alternative that was rejected.

| # | Decision | Alternative rejected | Why |
|---|---|---|---|
| D1 | The tool **proposes**; counsel classifies. Every result is labelled a proposal for legal review and carries its reasons and articles. | A confident "your category is X" | A compliance tool that hides its reasoning is either ignored by Legal or, worse, trusted without review. Reasons make it checkable in minutes. |
| D2 | Missing screening answers give **insufficient information**, never minimal risk. | Default unanswered flags to false | The expensive error is a high-risk system classified minimal because a box was left empty. |
| D3 | An Art. 6(3) derogation claim is never accepted by the tool; it goes to counsel, and it is rejected outright where the system profiles people. | Accept the owner's claim | The last subparagraph of Art. 6(3) excludes profiling; beyond that, whether a task is "narrow" or "preparatory" is a legal judgement, not a field. |
| D4 | The AI literacy target is an **internal policy setting** (`--literacy-target`, default 80%), stated as such in the pack. | Present a coverage threshold as the legal requirement | Since the 2026 amendment, Art. 4 asks for measures supporting literacy and no guaranteed level. Presenting 80% as the law would be wrong. |
| D5 | All article references and dates live in one versioned rules file with the date it was checked. | Rules in code | The law moved twice in 2026 (application dates and Art. 4 wording). Counsel can read and correct a JSON table; they will not read Python. |
| D6 | Obligations are filtered by the organisation's **role** for each use case (provider, deployer, both). | One obligation list per category | An insurer that buys a CV-screening tool and one that builds its own pricing model face different duties; mixing them overstates the work or hides it. |
| D7 | "Done" evidence without a reference counts as **partial**. | Trust the status column | Readiness reported on unchecked ticks is how programmes discover gaps at audit. |
| D8 | Markdown and JSON pack, no app, for v0.1. | A web dashboard | The committee paper is a document; the JSON lets the GRC tool or a dashboard read the same result later. |
| D9 | The pack never uses the words "compliant" or "certified" (tested). | Summarise green as "compliant" | Green means every listed obligation has evidence with a reference, which is narrower than compliance. The wording keeps the claim honest. |
