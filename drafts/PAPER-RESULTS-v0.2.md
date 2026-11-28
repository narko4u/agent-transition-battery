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

| run | held-out delta | improved | regressed | exact p | note |
|---|---|---|---|---|---|
| 80 tasks, 18 steps | -1.7 on holdout | 0 | 1 | - | 62 of 80 tasks produced no gradient |
| 200 tasks, one pass | +6.7 on holdout | 4 | 0 | 0.125 | below the preregistered bar |
| 200 tasks, three passes | +3.3 on holdout | 5 | 3 | 0.7266 | 398 of 600 visits had no gradient |
| 200 tasks, three passes | -3.3 on second holdout | 2 | 4 | 0.6875 | sign flip, guard breached |

The one-pass run produced the only positive weight result in the programme and it did not clear the
bar of p under 0.05, because four discordant pairs is too few to distinguish an effect from luck.

The three-pass run was meant to give the loop its best shot: three times the update steps, 202
gradient steps in total, 130 minutes on a free T4. It moved the first holdout by 3.3 points, below the
declared 5, and moved the second holdout backwards by 3.3, which breached the preregistered guard
against a sign flip. The telemetry explains why better than the verdict does. Of 600 task visits, 398
were skipped because all four samples returned the same reward, and there is no group-relative
gradient when every sample agrees. The model solved at least one of four samples on 387 visits.

Compute was not the constraint. Disagreement was. We were reinforcing a pool the model could mostly
already solve.

### 6.3 Reflective prompt evolution, and what it actually optimised

We then took the optimiser out of our own hands. GEPA (MIT) evolves the text of a system prompt by
reflecting on scored failures. It was given a seeded instruction, sixty dev tasks drawn from the same
public benchmark, and the battery's own scorer: the family's test file executed in a subprocess.

Evolution moved the dev family from 0.633 to 0.733 in 933 calls, 47 minutes and $0.26. The winning
instruction was output hygiene rather than method: no markdown fences, no prose, exact function name,
never return empty. We read that as a modest finding about prompt hygiene and moved to evaluation.

Evaluation disagreed with the dev set, and then we found out why.

The task model spends part of its completion budget on internal reasoning before it emits code. At
900 tokens it sometimes spent all of it and returned an empty completion with `finish_reason=length`,
which the scorer recorded as a wrong answer. Sixteen of sixty failures in one arm and seventeen of
sixty in another were blank answers.

We repaired the client to retry at triple budget when a completion comes back empty, then re-ran the
same comparison under the same preregistered rule (P-004R).

| run | family | base | tuned | delta | improved | regressed | exact p |
|---|---|---|---|---|---|---|---|
| P-004 | dev, optimised | 38/60 | 44/60 | +10.0 | - | - | - |
| P-004R | holdout 1 | 52/60 | 51/60 | -1.7 | 0 | 1 | 1.0000 |
| P-004R repeat | holdout 1 | 52/60 | 47/60 | -8.3 | 0 | 5 | 0.0625 |
| P-004R | holdout 2 | 47/60 | 47/60 | 0.0 | 1 | 1 | 1.0000 |

The seed instruction was worth 52 of 60 on the first holdout and 47 of 60 on the second, not the 38
and 36 that the broken client reported. Against that floor, the evolved instruction is worth nothing
and may be worth less: no improvement in any arm, five regressions in one replication, and dead level
on the family it never saw.

Which leaves the question of what the optimiser gained ten points on. Its winning text said "never
return empty, no fences, no prose, exact function name". That is a description of the harness defect.
The search did not discover a better way to solve tasks. It discovered which hole in the instrument
paid, and it filled that hole, because the instrument rewarded any transformation of a blank answer
into code whether or not the code was right.

**The instrument is part of the hypothesis.** A scored instrument is a mirror: an optimiser pointed at
it will optimise the instrument first, because instrument defects are usually cheaper to fix than the
task. Any self-improvement claim that reports a dev gain without a clean, separately validated
measurement path is reporting, at least in part, the shape of its own instrument. We did not avoid
that error. We found it, and this is the record of it.

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

Improvement here is bounded by the instrument and by transfer, not by optimiser strength. We changed
the weights, changed the reward, and changed the instruction. The shape was identical, and in two of
the three routes the gain did not survive a clean measurement at all.

Three findings, in order of how much they should change someone else's practice.

**First, the dev pool has to have room.** The seed instruction solves 220 of the 307 MBPP tasks we
hold outside the evaluation families, 0.717. Of the 87 it fails, 79 score zero on a dense metric:
the code runs and the algorithm is wrong. A prompt optimiser cannot supply an algorithm, and a
reinforcement loop cannot learn from tasks where all four samples agree. Both of our search lanes were
climbing a slope that did not exist.

**Second, the instrument is part of the hypothesis.** GEPA's ten point dev gain was an instruction that
said "never return empty". Our client was returning empty completions when the model spent its whole
budget on internal reasoning, and scoring them as wrong answers. The optimiser found that hole and
filled it, because the instrument paid for filling it. This is not an exotic failure mode: it is what
an optimiser does by default, and it is invisible unless the instrument is validated separately from
the search.

**Third, disjointness has to be checked by task id, not by belief.** We reported a dev family as
disjoint from our evaluation families when it was the evaluation family, same sixty ids in the same
order, because we had verified a different pair and generalised. The run was still informative only
because one family had never been touched. A five line check, run on the same turn the family is used
and recorded in the report, removes this whole class of error. We now run it before every run.

What we would tell a team attempting this: preregister the rule and do not move it. Validate the
scoring path on tasks with known outcomes before letting any optimiser near it. Check disjointness by
identifier every time. Use at least 120 held-out tasks, because sixty cannot resolve five points. And
treat a dev-set gain as a hypothesis about your instrument until a frozen family says otherwise.

The one durable positive result in the programme is inference-time search: sample three solutions,
select the one that passes the most self-written tests, plus 8.0 and plus 10.5 points on 200 tasks at
p 0.0025 and p 0.0001. It works because nothing is fitted to a development set. Everything that was
fitted, by weights, by reward or by prompt, moved the surface it was fitted on and nothing else.
