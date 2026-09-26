"""Find vertices whose removal leaves no component larger than half the tree.

Adjacency is symmetrized and duplicate edges collapse. Loops, cycles and
disconnected graphs raise ValueError. Empty input returns []. Return the one or
two centroids in normalized graph order. Labels are arbitrary hashable objects.
Iterative subtree accumulation takes O(V + E) time and space.

>>> tree_centroids({0: [1], 1: [2], 2: [3]})
[1, 2]
"""

from algorithm_lab._graph import normalize_graph


def tree_centroids(graph):
    data = {v: set(rows) for v, rows in normalize_graph(graph, undirected=True).items()}
    if not data:
        return []
    if any(v in rows for v, rows in data.items()) or sum(map(len, data.values())) != 2 * (
        len(data) - 1
    ):
        raise ValueError("graph must be a tree")
    root = next(iter(data))
    parents, order = {root: root}, [root]
    for node in order:
        for neighbor in data[node]:
            if neighbor not in parents:
                parents[neighbor] = node
                order.append(neighbor)
    if len(order) != len(data):
        raise ValueError("graph must be connected")
    sizes, largest = dict.fromkeys(data, 1), dict.fromkeys(data, 0)
    for node in reversed(order[1:]):
        parent = parents[node]
        sizes[parent] += sizes[node]
        largest[parent] = max(largest[parent], sizes[node])
    return [v for v in data if max(largest[v], len(data) - sizes[v]) * 2 <= len(data)]
