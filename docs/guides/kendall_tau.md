# Compare rankings while accounting for ties

[Guide index](../README.md) · [Implementation](../../algorithm_lab/kendall_tau.py)

## Reasoning

For each pair of observations, compare whether the two axes order the pair
the same way or opposite ways. Concordant pairs add one and discordant pairs
subtract one. Tau-b divides by a tie-adjusted denominator using the number of
untied pairs on each axis. The direct implementation uses O(n squared)
comparisons and O(n) copied storage.

## Worked example

Run these statements from the repository root.

```pycon
>>> from math import isclose, sqrt
>>> from algorithm_lab.kendall_tau import kendall_tau
>>> kendall_tau([1, 2, 3], [30, 20, 10])
-1.0
>>> isclose(kendall_tau([1, 1, 2], [1, 2, 3]), 2 / sqrt(6))
True
>>> kendall_tau([1, 1], [1, 2])
Traceback (most recent call last):
...
ValueError: correlation is undefined for a constant axis

```

## Boundary to remember

Inputs must contain at least two paired finite numeric observations.
A constant axis has no untied pairs, so correlation is undefined and raises
ValueError. Numeric inputs are converted to floats; very large adjacent
integers can become tied after conversion. This is rank association, not
linear covariance.
