"""Internal validation for finite weighted graph edges and path costs."""

import math


def weighted_graph(graph, *, allow_negative=False):
    data = {node: list(neighbors) for node, neighbors in graph.items()}
    for edges in list(data.values()):
        for neighbor, weight in edges:
            if (
                isinstance(weight, bool)
                or not isinstance(weight, (int, float))
                or (isinstance(weight, float) and not math.isfinite(weight))
            ):
                raise ValueError("weights must be finite numbers")
            if not allow_negative and weight < 0:
                raise ValueError("weights must be nonnegative")
            data.setdefault(neighbor, [])
    return data


def path_cost(first, second):
    try:
        total = first + second
    except OverflowError as exc:
        raise ValueError("path cost exceeds the finite numeric range") from exc
    if isinstance(total, float) and not math.isfinite(total):
        raise ValueError("path cost exceeds the finite numeric range")
    return total
