# Maximize value with unlimited copies of each item within a capacity.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/unbounded_knapsack.py)

## Reasoning

For each item, scan capacities upward so the state at a smaller capacity can already include that same item. This permits repeated copies; a descending scan would instead enforce a zero-one limit.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.unbounded_knapsack import unbounded_knapsack

print(repr(unbounded_knapsack([2, 3], [3, 5], 7)))  # 11
```

## Boundary to remember

Weights are positive, values and capacity are nonnegative, and unused space is allowed. The function returns the best value, not the chosen item counts.

## Practice exercise

Maximize the value packed into a capacity when each available item type may be reused indefinitely.
