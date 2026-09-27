# Measure uncertainty after normalizing category weights

[Guide index](../README.md) · [Implementation](../../algorithm_lab/entropy.py)

## Reasoning

Normalize nonnegative category weights into probabilities and sum minus p times log base two of p. A category carrying all mass gives no uncertainty, while equal weights spread uncertainty evenly. Scaling all weights together does not change the probability distribution or its entropy.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.entropy import entropy
>>> entropy([9, 0, 0])
0.0
>>> entropy([1, 1])
1.0
>>> import math
>>> assert math.isclose(entropy([1, 2, 3]), entropy([10, 20, 30]))
>>> assert math.isclose(entropy([1e308, 1e308]), 1.0)

```

## Boundary to remember

These are category weights, not raw continuous observations or signed scores. Zero-weight categories contribute nothing, and at least one category must carry positive mass.
