# Track mean and variance without storing observations

[Guide index](../README.md) · [Implementation](../../algorithm_lab/running_stats.py)

## Reasoning

Welford's recurrence updates the mean and sum of squared deviations when
one observation arrives. It avoids subtracting two large nearly equal sums,
as a naive sum-of-squares formula would. The state consists of a count, mean,
and deviation total, so each update takes O(1) time and space. Population and
sample variance share that state but use different divisors.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.running_stats import RunningStats
>>> stats = RunningStats([2, 4, 6])
>>> stats.count, stats.mean, stats.variance(sample=True)
(3, 4.0, 4.0)
>>> stats.add(float("nan"))
Traceback (most recent call last):
...
ValueError: observations must be finite numbers
>>> stats.count, stats.mean
(3, 4.0)
>>> stats.add(8)
>>> stats.mean, stats.variance()
(5.0, 5.0)

```

## Boundary to remember

A failed add leaves state unchanged. extend applies items sequentially,
so accepted earlier items remain if a later item fails. Empty mean or variance
queries raise ValueError; sample variance needs at least two observations.
Inputs and intermediates must be representable as finite floating-point values.
