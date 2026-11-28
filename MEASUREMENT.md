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

### Counterbalanced replication (Senti's defect 2)

The first run loaded and scored the base arm before the tuned arm, so cache warm-up and load order
could have favoured one side. Repeated on tasks 0 to 59 with the order reversed, tuned arm first, in
a fresh process:

| Order | Base | Tuned | Delta |
|---|---|---|---|
| base first | 26/60 | 27/60 | +1.7 |
| tuned first | 26/60 | 27/60 | +1.7 |

Identical to the task. The order effect is zero on this set, the measurement is order-invariant, and
the null stands on both orderings. A replication that returns the same numbers is the only cheap
defence against an order confound, and it costs nothing here because the model already ships.

## 1.5B, same tasks: capacity helped, the update hurt

Same 120 held-out tasks, same tests, same procedure. Qwen2.5-Coder-1.5B with a LoRA trained on the
same 307 solutions.

| Model | Base | Tuned | Delta |
|---|---|---|---|
| 0.5B | 51/120 (0.425) | 55/120 (0.458) | +3.3 |
| 1.5B | 68/120 (0.567) | 61/120 (0.508) | -5.8 |

Two findings, and the second is the important one.

1. Capacity is not the binding constraint. The 1.5B base is 14 points better than the 0.5B base on the
   same tasks. The substrate improved exactly as expected.
2. The update made a stronger model worse: 10 tasks improved, 17 regressed, exact McNemar p 0.248. Three
   epochs at 2e-4 on 307 examples is enough to drift a model away from the behaviour the tests reward.

So the failure was never "the model is too small to learn". It is that a small, narrow supervised set
moves the model in the wrong direction. The next questions are about data and update strength, not
parameters.
