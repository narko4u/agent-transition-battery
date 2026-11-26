# Runs

One JSON report and one log per run. Reports are immutable once committed. A correction is a
new report with `supersedes` set to the old `report_id`.

Naming: `<test>-<family>-<date>-<letter>.json`.

- `conformance-*.json` are produced by the scripted adapters. They prove the runner works and
  are never capability results.
- `t5-python-basics-*.json` are real model runs against the eight held-out tasks in
  `python-basics-heldout`. Read the distribution, not the best run.

Every report must pass `python3 ttb.py validate <report>` and `python3 tools/check_reports.py`.
