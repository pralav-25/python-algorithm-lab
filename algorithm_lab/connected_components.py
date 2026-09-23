"""Return disjoint vertex sets in O(V + E) time and space.

Every listed edge is interpreted as undirected, even if given in one direction.
Components follow first-seen vertex order. Vertices must be hashable.

>>> connected_components({0: [1], 2: [], 3: [4]})
[frozenset({0, 1}), frozenset({2}), frozenset({3, 4})]
"""

from algorithm_lab._graph import normalize_graph


def connected_components(graph):
    data = normalize_graph(graph, undirected=True)
    visited, result = set(), []
    for start in data:
        if start in visited:
            continue
        stack, component = [start], set()
        visited.add(start)
        while stack:
            node = stack.pop()
            component.add(node)
            for neighbor in data[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
        result.append(frozenset(component))
    return result
