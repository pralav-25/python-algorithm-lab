"""Maximize value with unlimited copies of each item within a capacity.

Weights and values are equally long integer iterables. Weights are positive;
values and capacity are nonnegative. Bool is rejected. Unused capacity is
allowed and duplicate items are harmless. Return only the maximum integer
value, so tied packings need no selection; no items gives zero. O(n*C) time and
O(n + C) space excluding integer arithmetic. Inputs are copied and not changed.

>>> unbounded_knapsack([2, 3], [3, 5], 7)
11
"""

from algorithm_lab._validation import integer


def unbounded_knapsack(weights, values, capacity: int) -> int:
    integer(capacity, "capacity", minimum=0)
    weights, values = list(weights), list(values)
    if len(weights) != len(values):
        raise ValueError("weights and values must have equal lengths")
    for weight in weights:
        integer(weight, "weight", minimum=1)
    for value in values:
        integer(value, "value", minimum=0)
    best = [0] * (capacity + 1)
    for weight, value in zip(weights, values, strict=True):
        for limit in range(weight, capacity + 1):
            best[limit] = max(best[limit], best[limit - weight] + value)
    return best[-1]
