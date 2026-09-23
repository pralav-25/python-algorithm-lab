"""Distances from a source using a min heap; unreachable vertices map to infinity.

All weights must be finite nonnegative int/float values, excluding booleans.
Invalid edges are rejected even in disconnected components. A missing source is
isolated. Time O((V + E) log(V + E)), space O(V + E), allowing duplicate heap entries.

>>> dijkstra({'a': [('b', 4), ('c', 1)], 'c': [('b', 2)]}, 'a')
{'a': 0, 'c': 1, 'b': 3}
"""

import heapq
import itertools
import math

from algorithm_lab._weighted_graph import path_cost, weighted_graph


def dijkstra(graph, source):
    data = weighted_graph(graph)
    data.setdefault(source, [])
    distances = dict.fromkeys(data, math.inf)
    distances[source] = 0
    counter = itertools.count()
    queue = [(0, next(counter), source)]
    while queue:
        distance, _, node = heapq.heappop(queue)
        if distance != distances[node]:
            continue
        for neighbor, weight in data[node]:
            candidate = path_cost(distance, weight)
            if candidate < distances[neighbor]:
                distances[neighbor] = candidate
                heapq.heappush(queue, (candidate, next(counter), neighbor))
    return distances
