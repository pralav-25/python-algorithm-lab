# Fit a monotone sequence by pooling violations

[Guide index](../README.md) · [Implementation](../../algorithm_lab/isotonic_regression.py)

## Reasoning

Start with one block per observation. Whenever neighboring block means
decrease, pool their sums and counts, then check the new neighboring pair.
Repeating this process gives the nondecreasing least-squares fit without
reordering observations. Each block is pushed and removed at most once,
so the algorithm uses O(n) rational operations and O(n) space.

## Worked example

Run these statements from the repository root.

```pycon
>>> from fractions import Fraction
>>> from algorithm_lab.isotonic_regression import isotonic_regression
>>> fitted = isotonic_regression([4, 1, 2, 6])
>>> fitted
[Fraction(7, 3), Fraction(7, 3), Fraction(7, 3), Fraction(6, 1)]
>>> all(a <= b for a, b in zip(fitted, fitted[1:]))
True
>>> sum(fitted) == 13
True
>>> isotonic_regression([Fraction(1, 2), Fraction(3, 2)])
[Fraction(1, 2), Fraction(3, 2)]

```

## Boundary to remember

The fit is unweighted and accepts integers or Fractions, excluding booleans
and floats. Returned values are Fractions, even for integral results. Pooling
preserves the observation order; sorting the input would solve a different
problem. Empty input returns an empty list.
