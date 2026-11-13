# AGENTS.md

This repository is designed to be readable by humans **and agents**.

## Machine-readable sources

- `catalog/intents.json` — the Intent catalogue, **generated from the node** by `scripts/sync_catalog.py`: one entry per family, its kind, and the Intents under it with their own kind, parameters and answer fields. Never edit those fields by hand; `--check` fails when the file no longer matches the node. The tier, Category, priority score and mission map are the only hand-kept parts. Which module is live for an Intent is decided by the protocol's own competition, not by this file.
- `catalog/missions.json` — Season II mission → Intent dependency map.
- `seed/h2-bounties.json` — maintainer-reviewed seed candidates; only entries with `"publish": true` may be published by `make seed-h2`.
- GitHub Issues — live source of truth for public bounty state.
- `docs/EVALUATION_NEEDS.md` — optional public Category/Intent evaluation-need export contract, bounded aggregation and review-before-publish CLI. Example data is **fictional**, not current mainnet state.

## Rules for agents

1. Do not create speculative issues just because a potential improvement can be imagined.
2. Search open and closed Issues before proposing a new gap.
3. Start from **real demand, observed failure, or a verified time-sensitive release-coverage gap**, not from a desire to generate tasks.
4. Do not invent acceptance evidence.
5. Do not disclose security-sensitive information publicly.
6. Do not auto-claim multiple bounties unless a human operator can actually execute them.
7. A mission output or new Provider/model version is not automatically a new Intent. Prefer reusable intelligence primitives.
8. For `source:release` work, cite the canonical release source and never require a predetermined rank.
9. Do not invent customer demand, private commitments, provider endorsement, or usage to justify a public bounty.
10. For evaluation work, take an Intent's kind and what it needs from the node (`catalog/intents.json`, `docs/INTENTS.md`, `./tb intent <NAME>`), never from a name, an older Issue or on-chain readiness. A scoring module is registered on a family and scores only the Intents of the family's own kind, so a deterministic Intent under a judgment family has no module anyone can build for it: never ask for one. Not every Intent needs its own GitHub Issue, but every Intent must be findable in the catalogue with its real requirements. Keep the qualification material the network holds back secret.
11. No mechanical admission counter, source domain count, synthetic answer set or passing WASM output proves semantic correctness. Use reproducible independent evidence where possible.
12. Treat exported opportunity records as **triage proposals**. Never auto-claim, auto-approve, promise bounty rewards, or alter protocol Canonical Evaluator/Validator state from GitHub.
13. Do not imply that per-Intent protocol Evaluator emissions pay for merely supplying data or opening/closing GitHub work.

## Contributing evaluation work

The one description of the flow is in [CONTRIBUTING.md](CONTRIBUTING.md#contributing-evaluation-material-or-a-scoring-module): find what the Intent needs from the node, submit it through Anjoman, then `/submit` the reference here. GitHub approval and the network's own acceptance are separate decisions.

## Useful local commands

```bash
./tb map
./tb search <term>
./tb intent <INTENT>
./tb mission <mission-id>
./tb next
./tb needs /path/to/opportunities.json
```

With GitHub CLI auth:

```bash
./tb claim <issue>
./tb progress <issue> "<update>"
./tb submit <issue> "<proof>"
```

## Live Issue metadata

Seeded bounty Issues contain a hidden `telegraph-bounty` JSON marker for machine parsing. Treat the visible issue body and acceptance criteria as authoritative if they disagree with derived metadata.


## Public evaluation opportunity confidentiality

An Intent's name, its kind, what that kind needs and which families take which module are public: the node serves them to anyone and `docs/INTENTS.md` prints them. Do not publish, summarize, copy or quote internal node/indexer evaluation observations, hidden material, source-diversity or freshness statistics, verification thresholds, private evidence URLs, or material quality alerts in Issues, PRs, comments, logs or artifacts. `docs/EVALUATION_NEEDS.md` describes a separate Category-level projection used to publish internal triage findings; it is not the path a contributor follows. Automated evaluation GitHub issues are generic and unfunded review candidates; no direct work approval or new economic mechanism is implied.

## Permanent demand and product integration

- H2 is a filtered origin, not the complete bounty universe. Do not create H2-specific mission links for general customer/Anjoman needs.
- Anjoman jobs, documents, budget and permission records are private. Never open GitHub issues from raw user requests, customer data or private execution/evaluator diagnostics. See `docs/DEMAND_INTAKE.md`.
- A validated commercial Provider recruitment issue uses `opportunity:provider` and is **not** a claimable developer bounty. Use normal `work:*` + `status:open` Issues for actual approved development work.
- GitHub `status:done` is not an authoritative capability-ready notification, paid usage event or permission to resume a private job. Never trigger Anjoman execution or mint Explorer claims from GitHub closure alone.
