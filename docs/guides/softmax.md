# Normalize large scores without exponential overflow

[Guide index](../README.md) · [Implementation](../../algorithm_lab/softmax.py)

## Reasoning

Subtract the largest logit before exponentiating. This common shift
cancels when dividing by the total, yet ensures every exponent is nonpositive
and at least one exponential is exactly one. Normalization therefore avoids
overflow from large positive scores. The routine takes O(n) time and space
and returns probabilities in the original input order.

## Worked example

Run these statements from the repository root.

```pycon
>>> from math import isclose
>>> from algorithm_lab.softmax import softmax
>>> softmax([1000, 1000])
[0.5, 0.5]
>>> probabilities = softmax([1000, 1001, 1002])
>>> isclose(sum(probabilities), 1.0) and probabilities[0] < probabilities[1] < probabilities[2]
True
>>> all(isclose(a, b) for a, b in zip(probabilities, softmax([0, 1, 2])))
True
>>> softmax([5])
[1.0]

```

## Boundary to remember

A nonempty iterable of finite integer or float logits is required;
booleans are rejected. Very small tails can underflow to zero. Adding a common
constant preserves the mathematical distribution, while multiplying logits
changes its concentration. These are normalized scores, not automatically
calibrated predictions.
