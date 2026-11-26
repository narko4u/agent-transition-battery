# Agent Transition Battery

A public test battery for the claim that an AI agent has become an AGI agent.

Most claims of that kind are made on a capability snapshot. This repo treats the transition as
the closure of five loops and asks a system to run the tests, not to describe itself.

Status: **v0.1, reference runner implements T1 and T5**. T2, T3 and T4 are specified and not
implemented. Every result in `runs/` is an executed run with its report, its verifier hash and
its spend. Nothing here is a leaderboard of intelligence.

Read `SPEC.md` for the battery. Read `PAPER.md` for why the battery is shaped this way. The
paper is a draft, not a published result.

## The five loops

| Test | Question | Implemented |
| --- | --- | --- |
| T1 Retention | Does performance survive a context reset with only the store carried? | yes |
| T2 Transfer | Does experience on family A help an unseen family B? | specified |
| T3 Acquisition | Does cost to a fixed threshold fall on the third unseen family? | specified |
| T4 Curriculum | Does a self-generated task stream beat replay and a static set? | specified |
| T5 Self-modification | Is a change promoted only by a verifier the candidate cannot edit? | yes |

A system is named for the loop it closed. It does not get the label.

## Quick start

    python3 ttb.py hash-family families/python-basics
    python3 ttb.py run-t1 --family families/python-basics --adapter scripted:learner \
        --out runs/conformance-t1.json
    python3 ttb.py run-t5 --dev families/python-basics-dev \
        --heldout families/python-basics-heldout --procedure procedure.md \
        --adapter scripted:improver --out runs/conformance-t5.json
    python3 ttb.py validate runs/conformance-t5.json

The `scripted` adapters exist to prove the machinery. They are deterministic and they are
labelled as conformance runs, never as capability results.

For a real run, set `DEEPSEEK_API_KEY` and use `--adapter deepseek`. Any OpenAI-compatible
endpoint works with `TTB_BASE_URL` and `TTB_MODEL`.

## What v0.1 already shows

Six T5 runs on `python-basics`, identical settings, one candidate procedure per run:

- baseline held-out accuracy moved between 0.625 and 0.875 across identical runs (8 tasks)
- one run in six promoted a change, by one task
- total spend 0.053 US dollars, about 11 minutes of wall clock

That is the finding, not the promotion. At eight tasks the gate cannot tell a real improvement
from provider nondeterminism, and a single-run promotion is noise. The battery reports the
distribution and the spend so a reader can see that for themselves. The reports are in `runs/`,
immutable once committed.

## Report format

Every run writes a JSON report (`schema/run-report-0.1.schema.json`) and a log. The report
carries:

- the family or families, each with a SHA-256 of its verifier
- the system, the adapter and the call count
- the budget: dollar cap, wall cap, spend, wall time
- the metrics that decide the test
- the pass rules that were in force
- the adversarial arm: attempts, whether the verifier copy changed, whether the real verifier changed
- lineage: parent and child procedure hashes, promoted or not
- a `report_id` that is the SHA-256 of the report body

`ttb.py validate` recomputes the report id and checks the required fields. A report that fails
validation is not a result.

## Participating

The repo is built for three kinds of contribution:

1. **A task family.** A directory with `family.json` and one executable test per task. The
   test is the verifier. If it cannot fail, it is not a test.
2. **An adapter.** A small class with `solve`, `propose`, `attack`, `remember`, `reset_context`,
   `forget` and `describe`. Third-party systems are welcome.
3. **A run report.** A report produced by this runner, with its log and its spend. A row without
   an executed artefact is not listed.

See `CONTRIBUTING.md`. Code is Apache-2.0. The specification and the paper are CC BY 4.0.

## What this does not claim

- Passing does not prove general intelligence. It proves five loops are closed at the scale tested.
- The families are small. Breadth is the number of families, not the number of prompts.
- A failed test is the useful output. Report the loop that failed, not a composite score.
- No result here is evidence about any product, including ours.

Operator: Empire Labs Pty Ltd. Contact: contact@empirelabs.com.au.
