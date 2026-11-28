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

## The update rule was wrong, not the substrate

Gentler training (one epoch, lr 1e-4) also failed: hold60 base 0.5833, tuned 0.5167, minus 6.7 points,
3 improved, 7 regressed. One epoch at a tenth of the learning rate is 0.97 training loss, so the model
underfits the data and still loses capability.

A direct probe of three tasks explains it. Outputs are well-formed code in both arms, so nothing is
lost to parsing. What changed is the approach:

| task | base | LoRA |
|---|---|---|
| mbpp_2 | `list(set(list1) & set(list2))` | `[e for e in list1 if e in list2]`, duplicates survive, test fails |
| mbpp_4 | `heapq.nlargest(n, numbers)` | `sorted(heapq.nlargest(n, numbers), reverse=True)` |

The adapter taught the model the style of 307 solutions, terse code with no intermediate reasoning, and
that style replaced the base model's habit of reasoning toward a correct answer. Supervised imitation of
solutions is the wrong update rule here. It optimises resemblance to the training answers, not
behaviour the hidden tests reward.

This is the distinction SIA makes in its own framing: their weight lever is reinforcement on task
feedback, not supervised imitation. Our six routes have all been imitation, prompt engineering or
selection. None of them has ever optimised the thing that is actually scored.

## RLVR at 80 tasks: almost a no-op, and that is the finding

First run of reinforcement on task feedback rather than imitation. 80 training tasks, four samples each,
scored by executable tests, group-relative advantage, 1e-4, one epoch.

- 18 gradient steps in 49 minutes, because 38 tasks produced no passing sample and 24 produced four of
  four. Both are flat groups and carry no learning signal.
- Held-out: base 0.5833, tuned 0.5667, delta minus 1.7 points, **0 improved and 1 regressed**.

Compare the supervised runs on the same model and tasks: minus 5.8 and minus 6.7 points, with 10 and 3
tasks improved. RLVR left the model nearly untouched. One task moved out of sixty.

That is the useful result. Optimising the scored behaviour did not damage the model the way imitating
307 solutions did, which supports the diagnosis that the harm came from style imitation. It also shows
the real limit at this budget: 18 update steps is not training, it is a nudge.

To get a real test we need update steps in the hundreds. The Colab T4 run at 200 tasks produces roughly
100. Anything beyond that means multiple epochs over the mixed-outcome tasks, or a reward that is not
binary pass/fail so that more samples carry signal.

## P-004: GEPA prompt evolution, dev to held-out

GEPA (MIT, `gepa-ai/gepa`) evolved the solver instruction against executed tests on
`mbpp-practice60`, a dev family with zero overlap with the training pool, hold60 or test60.
Seed 0.6333, best 0.7333 after 933 calls, 47 minutes, $0.2567. The evolved text is output
hygiene: no fences, no prose, exact function name, never empty.

| family | base | tuned | delta | up | down | exact p |
|---|---|---|---|---|---|---|
| practice60 (dev, optimised) | 38/60 | 44/60 | +10.0 | - | - | - |
| mbpp-hold60 | 38/60 | 39/60 | +1.7 | 5 | 4 | 1.0000 |
| mbpp-test60 | 36/60 | 38/60 | +3.3 | 5 | 3 | 0.7266 |
| combined held-out | 74/120 | 77/120 | +2.5 | 10 | 7 | 0.6291 |

Verdict under P-004: **fail**. It needed +5 points and p < 0.05 on hold60.

The decay is six to one. Ten points on the family it optimised, one and a half points on a sibling
sixty from the same benchmark. Both held-out directions are positive and neither is significant, so
the honest reading is "no detectable transfer", not "slightly better".

This is the third route to give the same shape: supervised weights (+3.3 on 120, p 0.557), RLVR
weights (-1.7, 0 of 60 improved), and now reflective prompt evolution (+2.5 on 120, p 0.629).
Every gain has been on the surface being optimised and has not crossed to the surface being tested.

## Correction: P-004 was optimised on the evaluation family

Recorded 2026-11-28, after the run and before publication.

`families/mbpp-practice60` is `families/mbpp-hold60`: identical task ids, identical order,
sixty of sixty. I had verified that the *weight training pool* was disjoint from the evaluation
families and reported that as if it also covered the GEPA dev family. It did not.

Consequences, stated plainly:

- The GEPA dev score and the hold60 result are the same sixty tasks. The hold60 arm is in-sample.
- The only genuinely held-out family in P-004 was test60, where the evolved instruction went
  36/60 to 38/60, +3.3, five up and three down, exact p 0.7266.
- Therefore P-004 is void as a transfer test and must not be quoted as one. The surviving claim
  is narrower and still negative: on the only unseen family, the gain was 3.3 points and not
  significant.

Second defect found in the same audit: DeepSeek Flash spends its whole allocation on internal
reasoning at small `max_tokens` and returns an empty completion with `finish_reason=length`.
At 900 tokens, 16 of 60 base failures and 17 of 60 test60 base failures were import errors, which
is what an empty answer looks like once it reaches the scorer. Both arms in P-004 were affected
equally, so the comparison survived, but the absolute rates were depressed and the noise inflated.

Fixes now in the tooling: `tools/lm.py` retries once at triple budget when content is empty and
counts the retries; every report carries `empty_completions`; dev families must be compared by
task id against every evaluation family before a run, not after.

The new dev pool is `families/mbpp-devpool`, built from MBPP tasks 120 and above in mbpp-basics,
307 tasks, verified zero overlap with hold60 and test60. It is scored once with the seed
instruction so that tasks the model already solves can be filtered before any search.
