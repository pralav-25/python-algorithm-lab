# Choose a center under unequal observation counts

[Guide index](../README.md) · [Implementation](../../algorithm_lab/weighted_median.py)

## Reasoning

Sort value-weight pairs and accumulate their weights. The first value reaching half the total is a lower weighted median and minimizes weighted absolute deviation. Integer weights keep the halfway decision exact even for very large counts.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.weighted_median import weighted_median
>>> values, weights = [2, 8, 20], [1, 3, 1]
>>> center = weighted_median(values, weights)
>>> center
8
>>> cost = lambda point: sum(weight * abs(value - point) for value, weight in zip(values, weights))
>>> assert cost(center) == min(cost(point) for point in range(2, 21))
>>> weighted_median([2, 8], [1, 1])
2

```

## Boundary to remember

Weights must be nonnegative with positive total mass. At an exact halfway tie, this API chooses the lower observed value rather than averaging the two central values.
