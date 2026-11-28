# Draft section for PAPER v0.2

## 6. Three routes to improvement, and what transferred

We ran three mechanisms for improving an agent on the same battery, each under a rule written
down before the run. This section reports what happened, including the case where the answer was
that nothing transferred.

A protocol here is a written prediction with a stopping rule: the family to be evaluated, the
minimum effect, and the significance threshold. A result that misses the rule is recorded as a
failure regardless of how promising it looked. Rules are in `runs/protocols/` and are committed
before the run. The exact test is McNemar's, two-sided, on discordant pairs only.

### 6.1 Supervised weights

Two open models were fine-tuned with LoRA on 307 MBPP solutions with executed tests, then scored
on the same sixty held-out tasks with and without the adapter.

| model | held-out delta | improved | regressed | exact p |
|---|---|---|---|---|
| Qwen2.5-Coder-0.5B | +3.3 on 120 | 15 | 11 | 0.557 |
| Qwen2.5-Coder-1.5B | -5.8 on 120 | 10 | 17 | 0.248 |
| 1.5B, gentler schedule | -6.7 on 60 | 3 | 7 | 0.62 |

The larger model had a better base score, 0.567 against 0.425, so capacity helped. The update hurt
it. Probing the failures showed why: on a task that the base model solved with `list(set(a) & set(b))`,
the tuned model wrote a duplicate-preserving list comprehension, and where the base chose
`heapq.nlargest` the tuned model sorted the whole list. The update taught the style of the solutions
and displaced the judgement that selected the right tool.

### 6.2 Reinforcement on executed tests

The same model was then trained with group-relative advantages computed from its own samples, scored
by hidden executable tests, with no reference solutions. This optimises the behaviour that is scored
rather than the text of a solution.

| run | held-out delta | improved | regressed | note |
|---|---|---|---|---|
| 80 tasks, 18 steps | -1.7 on 60 | 0 | 1 | 62 of 80 tasks flat |
| 200 tasks, one pass | +6.7 on 60, p 0.125 | 4 | 0 | below the preregistered significance bar |
| 200 tasks, three passes | see P-003 | | | |

The 200-task run produced the only positive weight result in the programme and it did not clear the
bar of p under 0.05, because four discordant pairs is too few to distinguish an effect from luck.
We report it as unconfirmed rather than as a win.

### 6.3 Reflective prompt evolution

We then took the optimiser out of our own hands. GEPA (MIT) evolves the text of a system prompt by
reflecting on scored failures. It was given the seeded instruction, sixty dev tasks drawn from the
same public benchmark, and the battery's own scorer: the family's test file executed in a subprocess.

Evolution moved the dev family from 0.633 to 0.733 in 933 calls, 47 minutes and $0.26. The winning
instruction was output hygiene rather than method: no markdown fences, no prose, exact function name,
never return empty.

| family | base | tuned | delta | improved | regressed | exact p |
|---|---|---|---|---|---|---|
| dev, optimised | 38/60 | 44/60 | +10.0 | - | - | - |
| held-out 1 | 38/60 | 39/60 | +1.7 | 5 | 4 | 1.0000 |
| held-out 2 | 36/60 | 38/60 | +3.3 | 5 | 3 | 0.7266 |
| held-out combined | 74/120 | 77/120 | +2.5 | 10 | 7 | 0.6291 |

**A correction we owe the reader.** The dev family and held-out 1 turned out to be the same sixty
tasks, compared by id after the run. Held-out 1 is therefore in-sample and is reported here only to
show that even in-sample the gain was 1.7 points on the binary outcome. The only genuinely unseen
family in this experiment is held-out 2, where the change was 36 to 38 of 60, five up and three
down, exact p 0.7266. Neither row supports a transfer claim.

**A defect in the measuring instrument.** The task model spends part of its completion budget on
internal reasoning before emitting code. At a 900 token limit it sometimes spent all of it and
returned an empty completion with `finish_reason=length`, which the scorer recorded as a wrong
answer: 16 of 60 failures in one arm and 17 of 60 in another. Both arms were affected equally, so
the comparison stands, but the absolute rates are depressed and any future work should report the
count of empty completions alongside the score.


### 6.4 The one thing that did transfer

Inference-time search, not learning. Sampling three solutions and selecting the candidate that passes
the most self-written tests beat one-shot on 200 tasks twice, by 8.0 points (131 to 147, p 0.0025) and
10.5 points (131 to 152, p 0.0001). Nothing is fitted to a dev set: the selection happens per task at
inference, so there is no pool of tasks to overfit. That is a statement about where the improvement
came from, not a claim that the gain generalises beyond the named evaluations, which we did not test.

That distinction is the finding. Every mechanism that learned from a development set produced a gain
that lived only on that set. The mechanism that learned nothing, and instead spent test-time compute
per task, improved unseen tasks reliably.

### 6.5 What this suggests

Improvement here is bounded by transfer, not by optimiser strength. We changed the weights, changed
the reward, and changed the instruction, and the shape was identical: a gain on the surface being
optimised that did not cross to the surface being tested.

Two explanations are live and we cannot separate them with this data. The first is that sixty-task
families are too small: with a base near 0.63 there are about twenty-two failures, and an optimiser
finds the ones that are cheap to flip, which are not the ones that generalise. The second is that
the model has already saturated the easy behaviour and the remaining failures are beyond a small
model regardless of instruction or adapter.

Either way the practical consequence is the same, and it is the recommendation we would give any
team running this kind of work: preregister the rule, use at least 120 held-out tasks, keep the
development family disjoint from the evaluation families, and treat a dev-set gain as a hypothesis
rather than a result.
