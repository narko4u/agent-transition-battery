# Noise floor, measured

Same prompt, same tasks, same model, temperature 0, run five times.

| Run | Accuracy |
|---|---|
| SM-004 baseline | 0.800 |
| trace baseline | 0.880 |
| noise 1 | 0.860 |
| noise 2 | 0.860 |
| noise 3 | 0.840 |

Mean 0.848, standard deviation 0.030, so a two-sigma band of about six points on fifty tasks.

Worse: when the two arms carry the identical prompt, between two and eight tasks out of fifty
still disagree, 5.7 on average, about eleven percent. That is the model giving different code to
the same question at temperature zero.

## What this means

SM-004 reported four tasks improved and one regressed. The identical-prompt control produces
four-and-a-bit disagreements by itself. The difference was noise, and the gate was right to
refuse it.

The trace procedure scored below its own baseline. Also noise.

Any effect smaller than about six points is not measurable with this design. A one-run A/B on
fifty tasks cannot settle a question about a prompt.

## The rule this implies

A candidate earns promotion only when its mean over at least three runs exceeds the baseline mean
by two standard deviations of the baseline's own repeats, on the same task set, with the same
number of runs. That threshold is roughly 0.91 against a 0.848 baseline, and it is honest about
what fifty tasks can see.

Detecting a five point gain needs a suite several times larger, or a measurement with less
variance than a language model at temperature zero.

The rule is written here and not applied. Changing the gate that judges me is not a decision I
should take alone.
