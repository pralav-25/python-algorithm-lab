"""Return (maximum value, selected indices) for an integer-capacity 0/1 knapsack.

Weights and capacity are nonnegative integers; values are integers and may be
negative. Each item is available once, including zero-weight items. Ties keep the
previous solution, excluding the current item. Time and space O(n * (capacity + 1)).

>>> knapsack([2, 3, 4], [3, 4, 5], 5)
(7, [0, 1])
"""


def knapsack(weights, values, capacity: int) -> tuple[int, list[int]]:
    weights, values = list(weights), list(values)
    if len(weights) != len(values):
        raise ValueError("weights and values must have the same length")
    if isinstance(capacity, bool) or not isinstance(capacity, int) or capacity < 0:
        raise ValueError("capacity must be a nonnegative integer")
    if any(isinstance(w, bool) or not isinstance(w, int) or w < 0 for w in weights):
        raise ValueError("weights must be nonnegative integers")
    if any(isinstance(v, bool) or not isinstance(v, int) for v in values):
        raise ValueError("values must be integers")
    table = [[0] * (capacity + 1)]
    for weight, value in zip(weights, values, strict=True):
        previous = table[-1]
        row = previous[:]
        for available in range(weight, capacity + 1):
            row[available] = max(row[available], previous[available - weight] + value)
        table.append(row)
    selected, available = [], capacity
    for item in range(len(weights), 0, -1):
        if table[item][available] != table[item - 1][available]:
            selected.append(item - 1)
            available -= weights[item - 1]
    return table[-1][capacity], selected[::-1]
