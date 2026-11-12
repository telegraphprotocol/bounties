# Contributing

The fastest path is an existing bounty issue.

## 1. Pick `status:open`

Claim issues marked `status:open`. Triage reports remain proposals until a maintainer turns them into clear, verifiable work.

Prefer:

- `priority:p0`
- `priority:p1`
- `help wanted`
- `good first bounty`

## 2. Claim it

Comment:

```text
/claim
```

The bot records your claim and moves the issue to `status:claimed`. Several people can claim the same Issue, while it is `status:open`, `status:claimed` or `status:review`. Each claim has its own record, progress window and reward snapshot.

Keep your claim active with meaningful progress at least once every 72 hours:

```text
/progress Provider endpoint is live; integrating the reference fixtures now.
```

Stale claims are warned, then automatically released, one person at a time. Other people's claims are not affected.

To give up your own claim and withdraw its pending submission (a maintainer can release someone else's with `/release @user`):

```text
/release
```

## 3. Build against the acceptance criteria

Build to the acceptance checklist rather than the Issue title alone.

For Provider/Miner or Evaluator work, provide working evidence. When an Issue requires live Telegraph integration, the submission must serve or evaluate the specified Intent and pass the stated checks.

For App work, match the requested proof. Issues that require a live paid request, receipt, settlement, autonomous flow or other end-to-end evidence need a working demonstration.

## 4. Submit proof

Comment:

```text
/submit <link(s) and concise proof>
```

Example:

```text
/submit https://github.com/alice/weather-miner — live endpoint + three Telegraph request IDs + reference-test output in README
```

The issue moves to `status:review`.

## 5. Verification

A maintainer reproduces the acceptance criteria.

- Pass: `/approve @user` accepts that person's part (with one submission waiting, `/approve` alone is enough). If nobody else is still working on it and every box under "Done when" is ticked, the Issue is complete; otherwise a maintainer ticks the boxes as each part is verified and closes it with `/done`.
- Needs changes: `/changes @user <reason>`; that person is back to `status:claimed` with a fresh 72-hour progress window.
- Cannot continue: `/release`

Funded rewards follow the terms recorded when the active claim was created. The bot stores a visible snapshot and hash of the Issue's `## Reward` section at `/claim` time; payout also requires independent funding authorization.

## Reporting a new gap

Use the Issue chooser. Describe:

1. what useful outcome is blocked or what verified time-sensitive market coverage is missing;
2. evidence that the gap is real;
3. the reusable Intent/component involved, if known;
4. what observable result would close it.

For a major model/API/tool release, include the canonical release source, use existing Intents where they fit, and define success as fair measurement rather than a preferred rank. See [docs/RELEASE_COVERAGE.md](docs/RELEASE_COVERAGE.md).

Maintainers normalize proposals into the smallest reusable bounty.

## Contributing evaluation material or a scoring module

This is the one description of the flow. Everything else links here.

**GitHub is where the work is claimed, proven and approved. Anjoman is where the network
receives it.** Those are two decisions: a maintainer approving your part on an Issue does not
make the network use your work, and the network using it does not close the Issue.

### 1. Find out what the Intent actually needs

Look it up in [the Intent catalogue](docs/INTENTS.md), or run `./tb intent <NAME>`. Both are
generated from the node, so the kind they show is the kind the network really scores that
Intent as. What each kind needs:

| Kind | Evaluation material | Scoring module |
|---|---|---|
| **deterministic** | **Truth sources**: free public APIs (no key) that answer the Intent's question | None to build. The network's own comparator does the comparing. |
| **hybrid** | Truth sources **and** question pairs | An **evaluator adapter**, registered on the family |
| **judgment** | **Question pairs**: a real question with a better and a worse answer | An **evaluator adapter**, registered on the family |

A scoring module is registered on a **family** (`FX_NOW`), never on one Intent
(`FX_NOW_EUR`), and the family's own kind decides which kind of module it takes. A family's
module also scores only the Intents of the family's own kind. So a **deterministic Intent
under a judgment family has no module anyone can build for it**: one registered there waits
as `pending` with `awaiting_compatible_material` and never goes live. The catalogue says
which Intents those are, so check before you build. Don't infer requirements from an
Intent's name, from an older Issue, or from its on-chain readiness, which is a separate
thing from its kind.

If the node does not settle something, say so on the Issue and ask. Don't guess.

### 2. Submit it through Anjoman

Everything reaches the network through [Evaluate](https://anjoman.ai/dashboard/eval).
Every Intent name in the catalogue, and in each bounty Issue, links there with that Intent
already chosen. The guides are
[Contribute Evaluation Data](https://anjoman.ai/docs/scoring/contribute-evaluation-data) for
material and
[Build an Evaluator Adapter](https://anjoman.ai/docs/scoring/build-a-scoring-module) for a
module. Nothing is submitted by posting it on GitHub.

Then check what the network made of it, on the same page: each row of material ends up
`eligible` or `rejected` with a reason, and a module's registration shows its stage.

### 3. Link it back here

Comment `/submit` on the Issue with the Intent you worked on and the address you uploaded
from, or your module's registration id. A maintainer verifies it with the network's own
public reads, so give enough to find it. Your address is public once you post it; that is
your choice to make.

**No open Issue for the Intent you care about?** You can still contribute: the network takes
material for every Intent in the catalogue whether or not a bounty exists. An Issue is how a
bounty gets claimed and approved, not permission to contribute.

### Quality

Material has to fit the Intent's real scope, not just its name: the right place, time,
language and parameters. Prefer independently sourced references to repackaged labels, keep
the upstream provenance, and mark a synthetic answer as synthetic. A row that passes the
format checks is not thereby correct. An unranked Intent may still be routable, and should be
described that way rather than as broken.

## Contribution quality

This repository expects focused, verifiable contributions:

- search open and closed Issues before proposing work;
- claim only work you can actively execute;
- run and inspect generated code before submission;
- provide authentic request IDs, transactions, benchmarks and screenshots;
- propose a new Intent only for a reusable intelligence primitive;
- report exploitable vulnerabilities through the private security channel.

Repeated low-signal behavior may be closed without review.

## Security

Follow [SECURITY.md](SECURITY.md) for secrets and exploitable vulnerability details.


## What stays out of a public Issue

An Intent's name, its kind and what that kind needs are public: the node serves them to
anyone and [the catalogue](docs/INTENTS.md) prints them. What does not go in a public Issue,
PR or comment: test distributions, missing-reference counts, source concentration, the
qualification inputs and answers the network keeps back, private diagnostic links and
customer payloads. Send those to maintainers through the channel in
[SECURITY.md](SECURITY.md), and they confirm sensitive scope privately before opening or
approving funded work.

## Demand and Provider opportunities

New requests begin in triage. Anjoman and user needs require prior authorization and a sanitized public description; see [Demand intake](docs/DEMAND_INTAKE.md). Keep private prompts, files, customer identity, hidden evaluator cases and exploitable weaknesses in their authorized systems.

`opportunity:provider` Issues invite established independent services to discuss onboarding. They use the listed commercial contact path instead of the `/claim` development workflow. Other `status:open` bounties follow the claim, submit and verification process above.

## Pull requests

Most bounty deliverables—a Miner, Evaluator or App—live in **your own repository**. Submit their proof through `/submit` on the Issue. Open a pull request here when changing this repository itself:

- catalogue fixes in `catalog/` (then run `python scripts/generate_docs.py`);
- a proposed gap in `seed/h2-bounties.json` (it stays `publish: false` until a maintainer approves it);
- fixes to `tb`, the bounty workflows, validation scripts or tests;
- documentation and fictional examples under `examples/`;
- a bounty whose Issue explicitly asks for a change here: reference it with `Closes #123`.

Keep these materials out of public pull requests:

- evaluation material, hidden cases or qualification data;
- private diagnostics, customer data, credentials or exploit details;
- edits to reward terms or approvals;
- bulk generated changes nobody asked for.

Run `python scripts/prepush.py` before pushing. CI runs the same check on Linux and Windows.

The bot receipt confirms that a command was accepted. A maintainer may rerun the
original canceled or failed command job; replay protection prevents a second claim
from the same accepted command. Editing a comment does not issue another command.
Every submission requires approval from a maintainer other than its claimant and
submitter.

## Working on this repository itself

Changes to scripts, workflows, schemas or docs follow normal pull-request flow (see [GOVERNANCE.md](GOVERNANCE.md)).

Requirements: Python 3.10+ and Node.js 20+. No other dependencies.

```bash
npm test                      # JS and Python tests
python scripts/prepush.py     # full structural check (what CI runs)
python scripts/generate_docs.py   # regenerate docs/INTENTS.md, MISSIONS.md, NETWORK_MAP.md after editing catalog/
```

On Windows use `tb.cmd` (or `python tb`) in place of `./tb`. `make` is optional; every target wraps the commands above.
