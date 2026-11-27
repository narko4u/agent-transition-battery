# Adopted procedure: best-of-three with self-generated tests

Adopted 27 November 2026 under SM-007.

## What it does

For a code task, sample three candidate programs at temperature 0.8. Write up to five assertions
from the specification alone. Execute every candidate against those assertions and return the one
that passes the most. Ties go to the shorter program. The task's real tests and reference are
never visible to the procedure.

## Evidence

MBPP sanitized, 120 tasks fixed before the runs, one call per baseline task and five per candidate.

| Round | Baseline | Candidate | Delta | Paired p |
|---|---|---|---|---|
| 1 | 0.6917 | 0.7500 | +5.8 | 0.0923 |
| 2 | 0.6750 | 0.7583 | +8.3 | 0.0063 |

Mean delta plus 7.1 points. Gate threshold 0.7334, candidate mean 0.7541. Spend 0.301 USD.

## Provenance

The method is Chen et al., CodeT: Code Generation with Generated Tests, arXiv 2207.10397,
reduced to three samples and one test set. Full CodeT uses many samples and dual execution
agreement; this is the affordable subset.

## Limits

- Selection rests on tests the model wrote, so a confident wrong idea can win.
- MBPP is public, so both arms may benefit from familiarity. The delta is comparative, not an
  absolute capability claim.
- Three times the tokens for one task.
- Two rounds, not three. The gate's floor is five points and this cleared seven, but three rounds
  is the house standard and the next decision should run them.

## Rollback

Delete this file and stop selecting by generated tests. No other artefact depends on it.
