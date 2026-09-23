"""Return strongly connected components as disjoint frozensets.

Kosaraju's two iterative DFS passes take O(V + E) time and space. Vertices are
hashable; neighbor-only vertices are included. Component order follows the
algorithm's finishing order, not sorting or a promised topological order.

>>> groups = strongly_connected_components({0: [1], 1: [0, 2], 2: []})
>>> set(groups) == {frozenset({0, 1}), frozenset({2})}
True
"""

from algorithm_lab._graph import normalize_graph


def strongly_connected_components(graph):
    data = normalize_graph(graph)
    visited, order = set(), []
    for start in data:
        stack = [(start, False)]
        while stack:
            node, expanded = stack.pop()
            if expanded:
                order.append(node)
            elif node not in visited:
                visited.add(node)
                stack.append((node, True))
                stack.extend((neighbor, False) for neighbor in reversed(data[node]))
    reverse = {node: [] for node in data}
    for node, neighbors in data.items():
        for neighbor in neighbors:
            reverse[neighbor].append(node)
    visited, result = set(), []
    for start in reversed(order):
        if start in visited:
            continue
        stack, component = [start], set()
        visited.add(start)
        while stack:
            node = stack.pop()
            component.add(node)
            for neighbor in reverse[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
        result.append(frozenset(component))
    return result
