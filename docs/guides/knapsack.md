# Choose a valuable subset under a capacity limit

[Guide index](../README.md) · [Implementation](../../algorithm_lab/knapsack.py)

## Reasoning

For each item and capacity, compare leaving the item out with adding it to the best solution for the remaining capacity using earlier items. Keeping the item dimension prevents accidental reuse. Traceback returns original indices, which lets a caller verify both the total value and the weight constraint.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.knapsack import knapsack
>>> weights, values = [3, 4, 5], [5, 7, 8]
>>> value, chosen = knapsack(weights, values, 7)
>>> value, chosen
(12, [0, 1])
>>> assert sum(weights[i] for i in chosen) <= 7
>>> assert sum(values[i] for i in chosen) == value
>>> knapsack([0], [4], 0)
(4, [0])

```

## Boundary to remember

Each item is available once, even when its weight is zero. Negative-value items need not be selected, and an empty selection is allowed. This differs from both unbounded and fractional knapsack.
