# Accumulate paired variation in one pass

[Guide index](../README.md) · [Implementation](../../algorithm_lab/online_covariance.py)

## Reasoning

Update the two running means and their cross-deviation total as each pair
arrives. Dividing that total by n gives population covariance; dividing by
n - 1 gives sample covariance. Subtracting the first pair as an origin helps
preserve small differences near a large shared offset. A paired Welford
recurrence uses O(n) time and O(1) state.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.online_covariance import online_covariance
>>> observations = [(1, 2), (2, 4), (3, 6)]
>>> online_covariance(iter(observations), sample=True)
2.0
>>> online_covariance([(10, 5)])
0.0
>>> online_covariance([(1, 6), (2, 4), (3, 2)], sample=True)
-2.0
>>> online_covariance([(10, 5)], sample=True)
Traceback (most recent call last):
...
ValueError: not enough observations

```

## Boundary to remember

Observations must be finite numeric pairs, and sample must be a boolean.
Population covariance needs at least one pair; sample covariance needs two.
The result has the product of the input units and is not normalized correlation.
An intermediate value outside floating-point range raises ValueError.

## Practice exercise

Measure inverse variation near large offsets and verify it against an
exact covariance of the unshifted integer observations.

```pycon
>>> from algorithm_lab.online_covariance import online_covariance
>>> from fractions import Fraction
>>> from math import isclose
>>> pairs = [(0, 10), (2, 4), (4, -2)]
>>> mean_x = Fraction(sum(x for x, y in pairs), len(pairs))
>>> mean_y = Fraction(sum(y for x, y in pairs), len(pairs))
>>> expected = sum((x - mean_x) * (y - mean_y) for x, y in pairs) / (len(pairs) - 1)
>>> shifted = [(10**12 + x, -(10**12) + y) for x, y in pairs]
>>> online_covariance(iter(shifted), sample=True)
-12.0
>>> assert isclose(online_covariance(shifted, sample=True), float(expected))
>>> assert online_covariance(shifted) == -8.0

```

Adding a constant to either coordinate does not change covariance.
Shifting by the first pair preserves the small deviations; sample and
population results still differ because their divisors are two and three.
