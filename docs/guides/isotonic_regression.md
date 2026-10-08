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

## Practice exercise

Repair an ordered sequence of measurements with one descending pair. Compare the squared error with sorting the measurements, and confirm that fitting an already repaired sequence changes nothing.

```pycon
>>> from fractions import Fraction
>>> from algorithm_lab.isotonic_regression import isotonic_regression
>>> measurements = [0, 3, 1, 2]
>>> fitted = isotonic_regression(measurements)
>>> fitted
[Fraction(0, 1), Fraction(2, 1), Fraction(2, 1), Fraction(2, 1)]
>>> def error(candidate):
...     return sum((observed - estimate) ** 2 for observed, estimate in zip(measurements, candidate))
>>> error(fitted), error(sorted(measurements))
(Fraction(2, 1), 6)
>>> assert isotonic_regression(fitted) == fitted

```

The violating values 3 and 1 share their mean, 2: their error is minimized by (3 - t)^2 + (1 - t)^2 at t = 2. The final observation already equals that mean. Sorting would move observations to new positions and therefore incur a different, larger error.
