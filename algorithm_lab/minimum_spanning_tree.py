"""Return (total_weight, selected_edges) for an undirected weighted graph.

Vertices are integers 0 through vertex_count-1. Weights are finite int/float values;
negative weights and parallel edges are valid. Self-loops are ignored. By default
nonempty disconnected graphs raise ValueError; require_connected=False returns a
minimum spanning forest. Equal weights keep input order. Time O(E log E + V), space O(E + V).

>>> minimum_spanning_tree(3, [(0, 1, 5), (1, 2, 2), (0, 2, 3)])
(5, [(1, 2, 2), (0, 2, 3)])
"""

import math

from algorithm_lab._weighted_graph import path_cost


def minimum_spanning_tree(vertex_count: int, edges, *, require_connected: bool = True):
    if isinstance(vertex_count, bool) or not isinstance(vertex_count, int) or vertex_count < 0:
        raise ValueError("vertex_count must be a nonnegative integer")
    rows = []
    for first, second, weight in edges:
        if any(
            isinstance(v, bool) or not isinstance(v, int) or not 0 <= v < vertex_count
            for v in (first, second)
        ):
            raise ValueError("edge endpoint is out of range")
        if (
            isinstance(weight, bool)
            or not isinstance(weight, (int, float))
            or (isinstance(weight, float) and not math.isfinite(weight))
        ):
            raise ValueError("weights must be finite numbers")
        rows.append((first, second, weight))
    parent, sizes = list(range(vertex_count)), [1] * vertex_count

    def root(vertex):
        while vertex != parent[vertex]:
            parent[vertex] = parent[parent[vertex]]
            vertex = parent[vertex]
        return vertex

    total, selected = 0, []
    for first, second, weight in sorted(rows, key=lambda edge: edge[2]):
        a, b = root(first), root(second)
        if a == b:
            continue
        if sizes[a] < sizes[b]:
            a, b = b, a
        parent[b] = a
        sizes[a] += sizes[b]
        selected.append((first, second, weight))
        total = path_cost(total, weight)
    if require_connected and vertex_count and len(selected) != vertex_count - 1:
        raise ValueError("graph is disconnected")
    return total, selected
