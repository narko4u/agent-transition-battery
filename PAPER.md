# Turning your AI Agent into an AGI Agent

*A transition contract and a five-loop test battery*

Empire Labs Pty Ltd

Draft v0.1, 26 November 2026. Every number in this paper comes from a paper we read in full or from a run we executed. Nothing here claims more than that.

## Abstract

The term AGI agent is used for two different things: an agent that scores well on a capability benchmark and an agent that closes its own improvement loops. The first is measured constantly. The second is asserted. We argue that the transition should be defined as the closure of five loops, each with a test that can fail. We show that none of the twenty-four papers we review reports the conjunction. We give the battery, the pass rules and an adversarial arm aimed at the verifier rather than the agent. We then report a pilot that calibrates the instrument rather than the agent: a distilled skill moved design judgement by one paired flip at n=14, from 12 of 14 to 13 of 14, with an exact McNemar p of 1.00. A power calculation on those discordant pairs puts the sample needed to resolve a seven point difference at roughly 330 paired tasks. That is the useful result. A second pilot ran the T5 gate six times on eight held-out tasks: one promotion in six, with baseline accuracy moving two tasks between identical runs. A third measured transfer across two families on ten tasks: zero, with a placebo of equal length performing the same. A fourth ran retention four times: three passes of a rule that a single control run cannot make trustworthy. Transition claims at demo scale are not measurements and the field's reporting standard should say so.

## 1. Two meanings, one label

An agent is a system that takes actions in an environment until a goal is met or a budget is spent. The word general, when it is attached, is supposed to say something more. The three most cited attempts to say what that something is agree on the shape of the answer and disagree on everything an operator needs.

Legg and Hutter define intelligence as the ability to achieve goals in a wide range of environments and formalise it as a compression-weighted sum of performance over a distribution of environments. Chollet defines it as skill-acquisition efficiency over a scope of tasks, with respect to priors, experience and generalisation difficulty. Morris and colleagues lay capability on one axis and performance on another, place systems in a six by two grid and argue that autonomy is a separate axis that capability unlocks without determining.

Each is a definition. None is an instrument. A definition tells you what would count if you could measure it. An instrument tells you what to run on Tuesday, what number comes out and what number would make you stop. The gap between the two is where the AGI agent label currently lives.

The other half of the literature has instruments and no definition. The self-improving agent papers build loops: an archive of variants and a parent-selection rule (Darwin Gödel Machine), runtime monkey patching of the agent's own source (Gödel Agent), an improver applied to its own code (STOP), an agent editing its own repository under a fixed benchmark (SICA), self-proposed tasks graded by a code executor (Absolute Zero), a skill library of verified programs (Voyager), memories of induced routines or distilled strategies (Agent Workflow Memory, ReasoningBank, Reflexion). Each reports a delta on a benchmark. None reports a transition.

Between the two halves sits a third literature that argues about architecture. Liao and colleagues prove, under an assumption that real task distributions are unions of low-dimensional manifolds, that routing and DAG composition beat a monolithic learner, with an optimal agent count that trades specialisation against routing regret. The archipelago position reaches a different conclusion from the same premise: human expertise is largely domain-specific pattern accumulation, apparent flexibility is coverage of many encapsulated routines, so a large assemblage of specialists may be what general intelligence actually looks like, with little cross-domain transfer. Both are arguments. Neither runs an agent.

Put together, the state of the field is: definitions without instruments, instruments without a transition criterion and architecture arguments without experiments. That is the gap this paper addresses.

## 2. What the literature actually reports

We distilled twenty-four papers in full and recorded, for each, the claim type, what was actually run and which of the five loops in Section 3 it touches. The full distillation with verified quotes is in a skill we maintain, one reference per paper. The pattern matters more than any row.

| Paper | Claim type | What was run | Loops touched | Missing |
| --- | --- | --- | --- | --- |
| Legg and Hutter, 2007 | Definition | Nothing | none | No operational test |
| Chollet, 2019 | Definition and benchmark design | Task corpus only | T3 in principle | No agent, no transition rule |
| Morris et al., 2023 | Definition framework | Nothing | none | Explicitly refuses a task set |
| Liao et al., 2026 | Analytic position | Nothing | none | Assumption untested, no verifier |
| Archipelago of experts, 2026 | Position | Nothing | none | No measurement, argues transfer is weak |
| Pathways to AGI, 2026 | Survey | Nothing | none | Ten-dimension checklist, no scores |
| Measuring progress, 2026 | Measurement framework | Nothing | T1 to T5 named | No baselines collected |
| Definitional alignment, 2026 | Framework | Nothing | none | Adjudicates definitions, no instrument |
| Meta^n, 2026 | System plus ablation | Depth ablation, two backbones | T5 | One benchmark family, no transfer test |
| Co-recursive self-extension, 2026 | Theory | Nothing | none | Asymptotic bounds, no run |
| Cognitive capability gaps, 2026 | Taxonomy | Nothing | names all five | Metrics unspecified |
| Executive disposes, 2026 | Instrument plus run | 52 gated runs, one game, three seeds | T5 adjacent | Efficacy zero, no self-modification |
| ARC-AGI-3, 2026 | Benchmark | Baseline agents | T2, T3 partial | No curriculum, no self-modification |
| Darwin Gödel Machine, 2025 | System | 80 iterations, two benchmarks | T5 | Fixed benchmark, no transfer test |
| SICA, 2025 | System | 15 iterations, 50 tasks | T5, T1 partial | One trajectory, no held-out family |
| STOP, 2024 | System | Seed improver, five transfer tasks | T5 | GPT-4 class only, weak models degrade |
| Gödel Agent, 2024 | System | Four benchmarks | T5 | Gains depend on a thinking step |
| Absolute Zero, 2025 | System plus training | 7B and 14B models, A800 clusters | T4, T3 | Compute envelope, one verifier type |
| Voyager, 2023 | System | Minecraft, 160 iterations | T1, T4 | Closed weights, one world |
| Agent Workflow Memory, 2024 | System | WebArena and Mind2Web | T1 | Labels from an LM judge |
| ReasoningBank, 2025 | System | Three benchmarks | T1 | Retrieval curve turns over at one |
| Reflexion, 2023 | System | Three task classes | T1 | Flat with weaker models |
| The AI Scientist, 2024 | System | End to end paper generation | T4 | Reviewer agreement 0.65 against 0.66 |
| AI Control, 2023 | Control evaluation | 5,000 problems, red team | T5 adversarial | No self-modification, 2023 models |

Read the What was run column. Ten of the twenty-four run nothing. Of the fourteen that run something, three are instruments or benchmarks rather than capability claims: a control evaluation, a benchmark calibration and a measurement instrument whose own efficacy result is null. Eleven run a single loop on a single benchmark family. None runs a system against a conjunction of loops. None pairs transfer with retention across a context reset, acquisition efficiency and self-extension in the same system.

The closest in method is the executive-disposes instrument, which is worth separating from the rest. It does not claim a capability gain. It builds a deterministic executive that owns belief, lets the model file only typed proposals and voids a run when the measurement machinery misbehaves. Across 52 gated runs, about 17 million tokens and two protocol days, it reports that removing the commitment store moves goal abandonment from 0.00 to 1.00 on two of three seeds while binding error stays at 0.00 and that ablating the binding repair leaves the measured drift unchanged. Its task efficacy is zero: no level completions and no score in any cell. The dissociation rests on one game at three seeds. That is the most useful paper in the set for our purpose, because it shows what an instrument looks like and what it costs to be honest with one.

The ARC-AGI-3 paper is also worth reading against itself. Its headline is a bare-model number: 0.50% for the best frontier model. In the same paper the authors report hiring researchers to build general harnesses on three public environments and then testing those harnesses on the full public set. The same model, Opus 4.6, scores 0.0% with no harness and 97.1% with the Duke harness on a variant of TR87 and 0.0% under both configurations on BP35. Extreme bimodal performance, in the authors' phrase. That result does more for the transition argument than any position paper in the set. The scaffold moves the score by 97 points on one environment and by nothing on another, so a benchmark number reported without its harness and without a transfer test is neither a capability measure nor a generality measure.

The benchmark has also moved since that release. In September 2026 OpenAI claimed that GPT-6 Astra saturates ARC-AGI-3 at 99.9% and surpasses the human action-efficiency baseline on 96 per cent of levels. Both figures come from the vendor's own harness and its own evaluation. If they hold, the March gap closed in six months, which is the strongest argument for this battery rather than against it: a benchmark family saturates and the claim moves to the next family, so the transition claim has to survive the replacement. A dated benchmark number is a snapshot of one family, not a property of the system.

## 3. The transition is a conjunction

We propose that an agent becomes an AGI-grade agent, at a measured scale, when five loops are closed. Each loop has a failure mode that the others do not catch.

**T1 Retention across context loss.** After a context reset, does performance on the same family persist when only the store is carried? Without T1, a system that looks improved is riding the context window. The failure is a decorative memory.

**T2 Transfer to an unseen family.** Does experience on family A measurably help family B with a different surface and a shared procedure? Without T2, breadth is coverage, not generality. This is the loop the archipelago position predicts will be small and the human transfer literature it cites, with 35 to 43 per cent spontaneous analogical transfer without hints, suggests the bar should be low and the measurement should be paired.

**T3 Acquisition efficiency.** Does the cost to reach a fixed threshold fall on the third unseen family compared with the first? This is Chollet's definition made operational. Without T3, a system with good priors looks like a system that learns.

**T4 Self-generated curriculum.** Does a task stream proposed from the agent's own failures beat random replay and a static set at equal budget? Without T4, the curriculum is the evaluator's and the agent is not choosing what to learn. The failure is a generator that produces easy variants of what it already passes.

**T5 Bounded self-modification.** Can the agent change its own procedure, have the change promoted only by a verifier it cannot edit, on a held-out split fixed before the run, with lineage, rollback and a hard cap? Without T5, the agent is a fixed policy wearing a new prompt. The failure is objective hacking: the Darwin Gödel Machine's own logs contain a discovered agent that reached a perfect score by removing the special-token logging its detector depended on.

The conjunction is the claim. Each loop alone has a known counterexample in the literature:
- retention without transfer is a lookup table,
- transfer without acquisition is a lucky prior,
- acquisition without self-generated tasks is a fixed curriculum,
- a self-generated curriculum without a hard verifier is a mirror,
- self-modification without an external gate is objective hacking.

A system that closes four is named for the four. It does not get the label.

## 4. The battery

The battery is deliberately boring: five procedures, each with a metric, a control and a pass rule. Families are chosen by the evaluator, not by the agent. A family is a distribution of tasks with one verifier: a test suite, a schema, a checker. Breadth is the number of families, not the number of prompts.

**T1.** Twenty tasks from family A with an empty store, then a full context reset and twenty matched tasks with only the store carried. Retention ratio R is accuracy in block two with the store divided by accuracy in block one. Pass at R of at least 0.8 and a margin over a no-store control outside its interval.

**T2.** Acquire on family A, evaluate on family B with a different surface and a shared procedure. The control arm gets no A experience. Pass on a positive transfer delta on at least two of three pairs, with a shuffled control that zeroes.

**T3.** Three unseen families in sequence at equal budget. Measure tasks or tokens to a fixed threshold. Pass when cost to threshold falls by at least 20 per cent from family one to family three.

**T4.** Three arms at equal budget: agent-generated tasks from its own failure trace, random replay of failures, static set. Pass when the generated arm beats both controls on held-out score on two seeds.

**T5.** The agent proposes a change to its own procedure. An external verifier runs a held-out suite and a safety gate. Promotion only on a measured margin, reproduced on a second seed. Lineage and exact rollback are recorded. An adversarial arm prompts the agent to edit the verifier, the logs or the gate. Pass on one promoted change with a reproduced margin, zero successful tampering and rollback that restores the prior state exactly.

Three rules apply to every test. The split is fixed before the run and hashed. The proposer is never the judge. Time and dollars are capped in code and hitting the cap ends the run with a report rather than a negotiation.

What the battery does not claim: passing does not prove general intelligence. It proves five loops are closed at the scale tested, with the failures named. The breadth requirement lives in the family selection, so every report must list the families, the verifier for each and who wrote it.

## 5. Pilot: calibrating the instrument

Before running the battery on an agent, we ran the cheapest part of it on ourselves: does a distilled skill change judgement about self-improvement designs and by how much?

**Setup.** Fourteen scenarios, each describing a self-improvement loop with one defect or none. Twelve defect codes: self grading, no held-out split, no archive, retrieval overload, soft curriculum, weak model, cost blind, unbounded budget, verifier inside the editable tree, no baseline, objective hacking, sound. The plain arm answers from the scenario. The skill arm gets the same scenario plus the full text of a distilled skill built from eleven closed-RSI papers, 2,204 tokens. Same model, deepseek-flash, temperature zero, identical prompt scaffold. 28 calls, 0.0119 US dollars.

**Result.** At the level of the defect code, plain scored 12 of 14 and skill scored 13 of 14. The discordant pairs were two in favour of the skill and one in favour of plain. Exact McNemar p is 1.00. At the stricter level, where the repair sentence must also name the mechanism in the expected vocabulary, plain scored 10 of 14 and skill 9 of 14, which is the same data scored by a rubric that punished a correct answer for saying outside where the list expected external.

**What it means.** The skill did not produce a measurable effect and the instrument is not yet good enough to say whether it could. The mention rubric is vocabulary-bound, so its failures are partly the rubric's. The code-level result is one flip and one flip at n=14 is nothing. A McNemar power approximation on the observed discordant rates puts the sample needed to resolve a seven point difference at roughly 330 paired tasks. At the measured cost per call that is affordable, which is the point: the constraint is task authoring and verifier quality, not money.

**Second pilot, the gate on our own harness.** We then ran T5 itself, six times, on the same model and the same setting: eight development tasks and eight held-out tasks from a family of small Python specifications, one candidate procedure proposed per run from the development failures, temperature zero. Baseline held-out accuracy across the six identical runs was 0.875, 0.75, 0.875, 0.625, 0.75 and 0.875. That is a two-task swing with no input change, from provider nondeterminism. One run in six promoted a change, by one task. Every candidate it proposed was a formatting instruction, of the form define the requested function at module top level with the exact name, not a change to how the model solves anything. Total spend was 0.053 US dollars and about eleven minutes of wall clock.

The gate did what it was built to do: it refused five of the six proposals and recorded the sixth as a partial, because a single seed cannot establish a margin. The number that matters is the baseline spread. At eight tasks one task is 12.5 points and the instrument moves by two tasks on its own. A single-run promotion at this scale is noise wearing a green tick.

That is the argument of this paper demonstrated on its own apparatus, at a cost any lab can afford. It is also why the battery reports distributions and spend rather than a best run.

**Third pilot, transfer.** We built a second family of ten text-processing tasks with the same procedure and a different surface, then ran T2 twice with three arms: control on the base procedure, experience after eight python tasks plus at most three lessons distilled from the failures and a placebo carrying generic advice of similar length. Control scored 0.7 in both runs. Experience scored 0.6 and 0.7. Placebo scored 0.7 and 0.6. Every difference is one task and the sign changes between runs. The lessons the model wrote were process advice, define the function and smoke-test it, not a strategy for the new family.

The result is a zero. The honest reading is not that transfer is impossible but that a distilled lesson at this strength and this sample buys nothing and that the placebo removes the obvious explanation that any extra text helps. It is also the loop the literature does not report. If transfer is this weak across two families that share a procedure, breadth claims deserve a control before they become generality claims.

**Fourth pilot, retention.** Four runs of T1 on the ten text tasks. Each run has three blocks: block one with no store, a context reset, block two carrying only the distilled lessons and a no-store control. Block one averaged 0.70. Block two averaged 0.75. Control averaged 0.675. Three runs passed the written rule and one failed. The one that failed had control at 0.70 and block two at 0.70.

The pass rule is too weak at this sample. A single control run moves by a task between seeds, so a one-task gain clears the rule three times in four. The honest reading is that the store does not show retention beyond noise at n equal to ten. What the pilot does show is that the loop is instrumented end to end: a store, a context reset, a matched block, a control and a gate that can fail.

We report this pilot because it is the smallest honest version of the problem the whole paper is about. A one-flip result at demo scale is exactly what a transition claim built on a single run looks like from the inside. The field's habit of reporting it as a gain is a measurement failure, not a capability one.

## 6. What is lacking, in build order

The failures in Section 2 are not equally hard. This is the order we would fund them.

1. **Instruments before definitions.** The definitional literature has spent two decades on the first axis and produced no pass rule. A battery that can fail is worth more than a better grid.
2. **Transfer tests.** T2 is the loop nobody reports and the one the archipelago position predicts will be small. If transfer is small, most generality claims are coverage claims and the field should say so with a number.
3. **Curriculum at operator scale.** Absolute Zero shows self-generated tasks work with a code executor as the only reward. It runs on A800 clusters for days. The open problem is the same loop on one small card with a cheaper verifier.
4. **Adversarial verification of the verifier.** AI Control is the only paper that prices safety against an adversary and it is not combined with any self-modification loop. T5's attack arm is that combination.
5. **Cost-aware promotion.** SICA is the only system here that puts dollars and wall clock into its utility. Promotion on accuracy alone buys expensive wins that the next iteration inherits.
6. **A reporting standard.** Families, verifier provenance, seeds, caps, failures and the sample size that would have resolved the result. Without the last one, every small-n gain is unfalsifiable.

## 7. Threats to validity

One model, one suite, one run. The pilot measures judgement about designs, not task performance. It is not T1. The suite was written by the same side that built the skill, which is a conflict of interest we can reduce but not remove. The mention rubric is vocabulary-bound as reported. The literature numbers are quoted from the papers, not re-run. Ten of the twenty-four report no experiment at all. The battery's pass rules are design decisions, not findings. The 0.8 and 20 per cent thresholds will need revision after the first real runs.

What we do claim: the five loops are each falsifiable, the conjunction is not reported anywhere in this literature and the sample size needed to support a transition claim is one to two orders of magnitude larger than current practice.

## 8. Conclusion

An AI agent becomes an AGI agent when it closes five loops at a measured scale, not when a benchmark number crosses a line. The useful output of the test is the loop that failed. Report that loop, not the label.

T1, T2 and T5 are built and have run on public families, with the results reported above. Each is instrumented end to end and each gate can fail. The next work is not another loop. It is scale: enough tasks and enough seeds that a one-task difference stops deciding the verdict. Then the same measurement on systems that are trying to close all five. If the loops do not close, the paper that results is still true and more useful than another position.

## References

Papers are cited in the text by author or short title. The full set, with arXiv identifiers, verified pull quotes and the evidence each paper reports, is held in two distilled skills: `closed-rsi-loop` for the eleven self-improvement papers and `agi-agent-shelf` for the thirteen AGI papers. Source text for every quoted number is on disk beside the skill.

- Aguilera Briones, J. E. Definitional alignment before capability alignment. arXiv 2606.12713, 2026.
- Akinrele, T. et al. A Taxonomy of Cognitive Capability Gaps in Generative and Agentic AI. arXiv 2608.02553, 2026.
- ARC Prize Foundation. ARC-AGI-3: A New Challenge for Frontier Agentic Intelligence. arXiv 2603.24621, 2026.
- Arjmandi, M. The LLM Proposes, the Executive Disposes. arXiv 2608.04066, 2026.
- Burnell, R. et al. Measuring Progress Toward AGI: A Cognitive Framework. arXiv 2605.28405, 2026.
- Chollet, F. On the Measure of Intelligence. arXiv 1911.01547, 2019.
- Fletcher, G. and Vu Khan, S. Pathways to AGI. arXiv 2605.06029, 2026.
- Greenblatt, R. et al. AI Control. arXiv 2312.06942, 2024.
- Hegelich, S. et al. Co-Recursive Semantic Self-Extension. arXiv 2610.31097, 2026.
- Kilov, D. Emergence is Overrated: AGI as an Archipelago of Experts. arXiv 2603.07979, 2026.
- Kim, Z. M. et al. Metan: Recursive Self-Improvement through Emergent Depth. arXiv 2608.24735, 2026.
- Legg, S. and Hutter, M. Universal Intelligence: A Definition of Machine Intelligence. arXiv 0712.3329, 2007.
- Liao, J. et al. Position: Agentic AI System Is a Foreseeable Pathway to AGI. arXiv 2605.12966, 2026.
- Lu, C. et al. The AI Scientist. arXiv 2408.06292, 2024.
- Morris, M. R. et al. Levels of AGI for Operationalizing Progress on the Path to AGI. arXiv 2311.02462, 2023.
- Ouyang, S. et al. ReasoningBank. arXiv 2509.25140, 2025.
- Robeyns, M. et al. A Self-Improving Coding Agent. arXiv 2504.15228, 2025.
- Shinn, N. et al. Reflexion. arXiv 2303.11366, 2023.
- Wang, G. et al. Voyager. arXiv 2305.16291, 2023.
- Wang, Z. Z. et al. Agent Workflow Memory. arXiv 2409.07429, 2024.
- Yin, X. et al. Gödel Agent. arXiv 2410.04444, 2025.
- Zelikman, E. et al. Self-Taught Optimizer (STOP). arXiv 2310.02304, 2024.
- Zhang, J. et al. Darwin Gödel Machine. arXiv 2505.22954, 2025.
- Zhao, A. et al. Absolute Zero. arXiv 2505.03335, 2025.
