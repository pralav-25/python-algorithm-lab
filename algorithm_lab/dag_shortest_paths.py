"""Distances from source in an integer-weighted DAG, omitting unreachable nodes.

Input maps each node to a mapping of neighbor: integer weight. Negative costs
are allowed. Missing source and any directed cycle (even unreachable) raise
ValueError. O(V+E) time/space, excluding arbitrary-size arithmetic costs.

>>> dag_shortest_paths({'a': {'b': 2, 'c': 5}, 'b': {'c': -4}}, 'a')
{'a': 0, 'b': 2, 'c': -2}
"""

from algorithm_lab._validation import integer
from algorithm_lab.topological_sort import topological_sort


def dag_shortest_paths(graph, source):
    data = {
        node: {v: integer(w, "weight") for v, w in neighbors.items()}
        for node, neighbors in graph.items()
    }
    for neighbors in list(data.values()):
        for v in neighbors:
            data.setdefault(v, {})
    if source not in data:
        raise ValueError("source is not in graph")
    order = topological_sort(data)
    distance = {source: 0}
    for node in order:
        if node not in distance:
            continue
        for neighbor, weight in data[node].items():
            candidate = distance[node] + weight
            if neighbor not in distance or candidate < distance[neighbor]:
                distance[neighbor] = candidate
    return distance
