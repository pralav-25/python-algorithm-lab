# Compare distributions through their shared mixture

[Guide index](../README.md) · [Implementation](../../algorithm_lab/jensen_shannon_divergence.py)

## Reasoning

Normalize each weight vector independently, form their equally weighted
mixture, and average the two relative divergences to that mixture. A category
present on only one side still has positive mixture mass, avoiding an infinite
result. The symmetric divergence takes O(n) time and is measured in bits:
equal distributions give zero, while disjoint supports give one.

## Worked example

Run these statements from the repository root.

```pycon
>>> from math import isclose
>>> from algorithm_lab.jensen_shannon_divergence import jensen_shannon_divergence
>>> jensen_shannon_divergence([2, 6], [1, 3])
0.0
>>> jensen_shannon_divergence([1, 0], [0, 1])
1.0
>>> left, right = [1, 3, 0], [2, 0, 2]
>>> isclose(jensen_shannon_divergence(left, right), jensen_shannon_divergence(right, left))
True

```

## Boundary to remember

Vector positions must refer to the same categories in the same order.
Both sides need positive total mass and equal length; zero entries are allowed.
This returns divergence, not its square root, which is commonly used as a
distance. Tiny floating-point probabilities may underflow to zero.
