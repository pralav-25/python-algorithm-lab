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

## Practice exercise

Measure how one adjacent reversal affects an otherwise agreeing four-item ranking. Confirm that increasing transformations of the scores preserve the rank correlation.

```pycon
>>> from math import isclose
>>> from algorithm_lab.kendall_tau import kendall_tau
>>> first, second = [1, 2, 3, 4], [1, 3, 2, 4]
>>> correlation = kendall_tau(first, second)
>>> assert isclose(correlation, (5 - 1) / 6)
>>> assert isclose(kendall_tau([x * x for x in first], [100 * y for y in second]), correlation)
>>> round(correlation, 6)
0.666667

```

Among the six pairs, only the two middle items disagree, leaving five concordant pairs and one discordant pair. Neither axis has ties, so the denominator is six. Squaring these positive scores preserves order even though it changes their numeric spacing.
