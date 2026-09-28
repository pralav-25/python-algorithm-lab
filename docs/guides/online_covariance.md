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
