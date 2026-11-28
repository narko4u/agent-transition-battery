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

## Weight-level transfer, sixty plus sixty held-out MBPP tasks

The sixth route in the M2 attempt was not text. A LoRA adapter was trained on the first 120 MBPP
tasks and evaluated on tasks 61 to 120 and 0 to 59, neither of them in the training split.

| Set | Base | Tuned | Delta | Up | Down |
|---|---|---|---|---|---|
| tasks 61 to 120 | 25/60 | 28/60 | +5.0 | 9 | 6 |
| tasks 0 to 59 | 26/60 | 27/60 | +1.7 | 6 | 5 |
| combined | 51/120 | 55/120 | +3.3 | 15 | 11 |

Exact McNemar on the 26 discordant pairs gives p 0.557. The first set alone looks like a five-point
gain and is not one; that is the same small-sample trap as the earlier sixty-task procedure run, and
it is the reason the second set was run before anything was claimed.

Reproduction needs no API spend: `python3 tools/eval_local.py --family families/mbpp-hold60`.
