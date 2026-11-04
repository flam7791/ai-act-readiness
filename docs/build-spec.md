# Build spec

| Item | Value |
|---|---|
| What | A command-line MVP that turns an AI use-case portfolio, an evidence log and literacy data into an AI Act readiness pack for an executive committee |
| For whom | AI governance lead (user), chief data and AI officer (sponsor), in-house counsel (reviewer), executive committee (decides) |
| Stage | Prototype on synthetic data, designed for a two-cycle pilot |
| Platform | Python 3.10+, standard library only; CSV and JSON in, Markdown and JSON out |
| Must never | Present a proposal as a legal classification; say "compliant"; accept an Art. 6(3) claim on its own; guess a category from missing answers |
| Acceptance criteria | One per backlog story ([backlog.csv](team/backlog.csv)), each proved by a named test |
| Assumptions | The organisation already keeps a use-case register; owners can answer eight yes/no or coded questions; counsel will review proposals rather than write from scratch |
| Out of scope | GPAI provider duties, Annex I products, GDPR assessment, a user interface |
