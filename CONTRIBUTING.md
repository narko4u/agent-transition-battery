# Contributing

Three things can be contributed: a task family, an adapter, a run report.

## The one rule

**A result without an executed artefact is not a result.** A pull request that adds a row to
`registry/index.json` must also add the report and its log produced by `ttb.py`, and the report
must pass `ttb.py validate`. An issue that reports a score without the run is closed.

## Task families

- One directory under `families/`, with `family.json` and one test file per task.
- The test must be executable and must be able to fail. A test that passes on an empty solution
  is rejected in review.
- State in `family.json` who wrote the family and what the verifier is.
- Families are frozen once a report cites them. A change to a test changes the verifier hash and
  invalidates every report against it, so publish a new family instead.
- Do not submit a family whose tests you would not accept from a competitor. The verifier is the
  product here.

## Adapters

An adapter is a class with:

    describe() -> dict            name, model, adapter, version
    solve(task, store, procedure) -> str    returns candidate code
    propose(procedure, failures) -> str|None
    attack(verifier_dir) -> list[dict]
    remember(family, block, store)
    reset_context()
    forget()

Optional: `spend_usd()`, which the runner writes into the budget.

Adapters must not have network access beyond the model endpoint, must not write outside their
own temporary directory, and must not be given the held-out family at solve time. If your
adapter has file tools, its `attack` must make a real attempt, not a simulated one.

## Run reports

- Run the runner, commit the JSON and the log under `runs/`.
- Name the file `<test>-<family>-<date>-<letter>.json`.
- Reports are immutable once merged. A correction is a new report with `supersedes` set to the
  old `report_id`.
- Do not edit a report to change a status. Re-run it.
- State the seed, the spend and the number of tasks. A single run is labelled `single-run` and
  cannot support a promotion claim.

## Review and licensing

- Code is Apache-2.0. The specification and the paper are CC BY 4.0. By contributing you agree
  to those licences and to the Developer Certificate of Origin (`Signed-off-by` on every commit).
- One maintainer decision on claim language and on what enters the registry. Everything else is
  ordinary review.
- No claims of achieved AGI in the README, the registry or a report title. Name the loop.

## What we will reject

- A family whose tests came from the same source as the candidate's training data, unless you
  say so and the report carries a contamination note.
- A report that omits its spend or its verifier hash.
- A promotion from a single run.
- A submission that edits the scoring harness and asks to be listed anyway. That attempt is
  logged as a T5 adversarial result and the submission is closed.
