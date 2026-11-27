# What this suite can and cannot see

Four protocols were measured against the same forty tasks, same model, temperature 0, same
prompt on both arms. The question was how much of an A/B result is noise.

| Protocol | Same-prompt accuracy | Spread | Tasks that flipped |
|---|---|---|---|
| one run per arm, pass or fail | 0.800, 0.880, 0.860, 0.860, 0.840 | sd 0.030 | 5.7 of 50 |
| majority of three, pass or fail | 0.860, 0.840 | range 0.020 | 3.0 of 50 |
| partial credit, one test per case | 0.875, 0.825 | sd 0.035 | 3.0 of 40, mean gap 0.075 |

Three findings.

1. Temperature zero is not deterministic. The same prompt produced different code often enough
   to flip eleven percent of task outcomes.
2. Majority voting halves the flips at three times the cost. It buys quiet, not power.
3. Partial credit does not help here, because the failures are wholesale. A wrong function fails
   every case, so the score is almost binary anyway.

## The protocol this implies

A promotion decision needs three runs per arm, majority of three per task, and a candidate mean at
least two standard deviations above the baseline mean measured the same way. On forty tasks that
is roughly a seven point effect to clear the bar, at about 0.22 US dollars per decision.

Anything smaller needs more tasks, not a cleverer statistic. Fifty tasks cannot see five points,
and no amount of analysis changes that.

## The adopted procedure is not immune

On 27 November the same configuration, `bon3`, scored 0.8167 and 0.9000 on the same sixty tasks
inside one hour. Eight points apart with nothing changed. Any comparison that treats a single
run of a five point effect as a finding is measuring that spread, not the effect.
