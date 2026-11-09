# Track mean and variance without storing observations

[Guide index](../README.md) · [Implementation](../../algorithm_lab/running_stats.py)

## Reasoning

Welford's recurrence updates the mean and sum of squared deviations when
one observation arrives. It avoids subtracting two large nearly equal sums,
as a naive sum-of-squares formula would. This implementation first shifts
observations by the initial value to preserve small differences near large
common offsets. Population and sample variance share the shifted moment state
but use different divisors.

The reported mean is computed separately from an exact rational total of the
validated floating-point observations. Reconstructing it from a distant initial
offset could lose small residuals after cancellation. Each update uses a fixed
number of arithmetic operations and accumulators rather than retaining the stream;
the exact total's integer storage can grow with the observation count.

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
>>> RunningStats([1e16, -1e16, 3]).mean
1.0
>>> RunningStats([1e16, 1e16 + 2]).variance()
1.0

```

## Boundary to remember

A failed add leaves state unchanged. extend applies items sequentially,
so accepted earlier items remain if a later item fails. Empty mean or variance
queries raise ValueError; sample variance needs at least two observations.
Inputs and variance intermediates must be representable as finite floating-point
values. The exact total need not itself fit in a float: repeated equal large
observations can still have a finite mean and zero variance. Variance remains
a floating-point estimate, while the mean rounds the exact total only on output.
