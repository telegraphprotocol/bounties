# Glossary

Terms as this repository uses them. Protocol behaviour is defined by Telegraph itself; where this glossary and the protocol differ, the protocol wins.

| Term | Meaning |
|---|---|
| **Intent** | A reusable machine-intelligence task with a market of its own, such as `FX_NOW_EUR`. The catalogue is read from the node ([INTENTS.md](INTENTS.md)). Miners and Evaluators compete per Intent. |
| **Family** | The name a scoring module is registered on, and the prefix of the Intents under it: `FX_NOW` is the family of `FX_NOW_EUR`. A family has a kind of its own, and its module scores only the Intents of that kind. |
| **Kind / class** | How the network scores an Intent: **deterministic** (one right answer, checked against truth sources), **judgment** (open-ended, scored by an adapter) or **hybrid** (both). The node decides it, and it decides what the Intent needs. |
| **Category** | A group of related Intents, such as Climate & Weather. Evaluation scoring logic can be shared across a Category. |
| **Mission** | One of the 15 Season II application goals. A mission composes several Intents. A mission is application logic, not a new Intent ([MISSIONS.md](MISSIONS.md)). |
| **Season II / H2** | The hackathon proving ground built around the 15 missions. `source:h2` marks work that comes from it. H2 is one filter on the board, not the whole board ([H2.md](H2.md)). |
| **Miner / Provider** | A service that supplies intelligence for an Intent. The GitHub label stays `work:miner`; public text often says Provider. |
| **Evaluator** | A party that measures how good supplied intelligence is so Miners can be ranked. |
| **Canonical Evaluator** | The Evaluator the protocol currently recognises for an Intent. It is set by the protocol's own competition and verification, never by this repository or by catalogue metadata. |
| **Evaluator adapter** | A small model trained on the network's shared foundation model, registered on a judgment or hybrid family, that scores answers for every Intent of that kind under it. Ranking stays per Intent. |
| **Comparator module** | The code that compares a number in a miner's answer with the reference value, for a deterministic family. It has no model and only has to compute the network's fixed rule, so there is nothing better to build. |
| **Evaluation material** | What miners are scored on. **Truth sources** (free public APIs that answer a deterministic Intent's question) and **question pairs** (a real question with a better and a worse answer, for a judgment one). Submitted through Anjoman; see [CONTRIBUTING.md](../CONTRIBUTING.md#contributing-evaluation-material-or-a-scoring-module). The qualification material the network holds back stays secret. |
| **App / Agent** | A product or autonomous workflow that consumes Intents. Apps create demand and expose gaps. |
| **Gap** | Something the network needs that is missing or too weak: supply, evaluation, integration, tooling or release coverage. A gap becomes a public Issue only after maintainer triage. |
| **Bounty** | A claimable Issue (`status:open`) with objective acceptance criteria. It may or may not carry a reward. |
| **Provider opportunity** | `opportunity:provider`. A commercial recruitment listing for an already-operating service. Not claimable and never a bounty. |
| **Slot Issue** | One of several related Issues (1/3, 2/3, 3/3) used when the network needs several independent implementations. Each has its own claim and reward terms. |
| **Triage** | The first state of every public report (`status:triage`). A maintainer checks it is real, reusable, not a duplicate, safe to publish and verifiable before running `/open`. |
| **Claim** | Your recorded right to work an Issue, made with `/claim`. Several people can hold claims on one Issue. Yours is released after 72 hours without a `/progress` update. |
| **Release coverage** | Work that lets a newly released model, API or tool be measured fairly in an existing market. Success is fair eligibility, not a particular rank. See [RELEASE_COVERAGE.md](RELEASE_COVERAGE.md). |
| **Anjoman** | Telegraph's own product, and where evaluation material and scoring modules reach the network ([Evaluate](https://anjoman.ai/dashboard/eval)). Its jobs, documents and budgets are private and never published here. See [DEMAND_INTAKE.md](DEMAND_INTAKE.md). |
| **Explorer** | Telegraph's view of network state. This repository does not read from it directly. |
| **MACHINA** | A possible bounty payout asset. A reward counts only if the Issue names the asset and the conversion rule ([REWARDS.md](REWARDS.md)). |
| **V2** | The current Telegraph protocol generation referred to by the evaluation documents. |
