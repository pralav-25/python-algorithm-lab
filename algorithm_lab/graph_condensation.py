"""Return (components, dag) by collapsing each strongly connected component.

components is a list of frozensets; dag maps their integer indices to frozensets
of neighboring indices. Parallel edges collapse; internal edges vanish. Indices
follow SCC traversal order and have no sorting promise. O(V+E) time/space.

>>> components, dag = graph_condensation({0: [1], 1: [0, 2]})
>>> sorted(map(len, components))
[1, 2]
>>> sum(map(len, dag.values()))
1
"""

from algorithm_lab._graph import normalize_graph
from algorithm_lab.strongly_connected_components import strongly_connected_components


def graph_condensation(graph):
    data = normalize_graph(graph)
    components = strongly_connected_components(data)
    membership = {node: i for i, group in enumerate(components) for node in group}
    dag = {i: set() for i in range(len(components))}
    for node, neighbors in data.items():
        for neighbor in neighbors:
            a, b = membership[node], membership[neighbor]
            if a != b:
                dag[a].add(b)
    return components, {i: frozenset(rows) for i, rows in dag.items()}
