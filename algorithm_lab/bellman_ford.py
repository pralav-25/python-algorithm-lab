"""Compute shortest distances, rejecting negative cycles reachable from source.

Unreachable vertices map to infinity; unreachable negative cycles are ignored.
All edge weights must be finite int/float values excluding booleans. A missing
source is isolated. Time O(VE), space O(V + E), including the input snapshot.

>>> bellman_ford({'a': [('b', 2), ('c', 5)], 'b': [('c', -4)]}, 'a')
{'a': 0, 'b': 2, 'c': -2}
"""

import math

from algorithm_lab._weighted_graph import path_cost, weighted_graph


def bellman_ford(graph, source):
    data = weighted_graph(graph, allow_negative=True)
    data.setdefault(source, [])
    edges = [(node, neighbor, weight) for node, rows in data.items() for neighbor, weight in rows]
    distances = dict.fromkeys(data, math.inf)
    distances[source] = 0
    for _ in range(len(data) - 1):
        changed = False
        for node, neighbor, weight in edges:
            if distances[node] != math.inf:
                candidate = path_cost(distances[node], weight)
                if candidate < distances[neighbor]:
                    distances[neighbor], changed = candidate, True
        if not changed:
            break
    for node, neighbor, weight in edges:
        if distances[node] != math.inf and path_cost(distances[node], weight) < distances[neighbor]:
            raise ValueError("a negative cycle is reachable from the source")
    return distances
