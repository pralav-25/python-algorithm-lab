"""Maximum bottleneck capacities from a source using a priority queue.

Directed edges have finite nonnegative int/float capacities excluding bool.
Return capacities for all vertices: the source has infinity (an empty path),
unreachable vertices have -1, and reachable zero-capacity paths have zero.
Hashable labels need not be comparable. All edges are validated, including
disconnected ones. O((V + E) log(V + E)) time and O(V + E) space.

>>> widest_path({'a': [('b', 3), ('c', 8)], 'c': [('b', 5)]}, 'a')
{'a': inf, 'c': 8, 'b': 5}
"""

import heapq
from itertools import count
from math import inf

from algorithm_lab._weighted_graph import weighted_graph


def widest_path(graph, source):
    data = weighted_graph(graph)
    data.setdefault(source, [])
    capacities = dict.fromkeys(data, -1)
    capacities[source] = inf
    serial = count()
    queue = [(-inf, next(serial), source)]
    while queue:
        negative, _, node = heapq.heappop(queue)
        capacity = -negative
        if capacity != capacities[node]:
            continue
        for neighbor, weight in data[node]:
            candidate = min(capacity, weight)
            if candidate > capacities[neighbor]:
                capacities[neighbor] = candidate
                heapq.heappush(queue, (-candidate, next(serial), neighbor))
    return capacities
