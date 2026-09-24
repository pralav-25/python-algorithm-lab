"""Iterative low-link analysis for a simple undirected adjacency mapping.

Asymmetric adjacency is symmetrized; duplicate edges collapse and loops are
ignored. Arbitrary hashable labels (including None) are supported.
"""

from algorithm_lab._graph import normalize_graph


def lowlink(graph):
    raw = normalize_graph(graph, undirected=True)
    data = {
        node: list(dict.fromkeys(v for v in neighbors if v != node))
        for node, neighbors in raw.items()
    }
    discovered, low, parent, children = {}, {}, {}, {}
    bridges, cuts = [], set()
    for root in data:
        if root in discovered:
            continue
        discovered[root] = low[root] = len(discovered)
        children[root] = 0
        stack = [(root, iter(data[root]))]
        while stack:
            node, neighbors = stack[-1]
            try:
                neighbor = next(neighbors)
            except StopIteration:
                stack.pop()
                if node in parent:
                    p = parent[node]
                    low[p] = min(low[p], low[node])
                    if low[node] > discovered[p]:
                        bridges.append((p, node))
                    if p in parent and low[node] >= discovered[p]:
                        cuts.add(p)
                elif children[node] > 1:
                    cuts.add(node)
                continue
            if neighbor not in discovered:
                parent[neighbor] = node
                children[node] += 1
                children[neighbor] = 0
                discovered[neighbor] = low[neighbor] = len(discovered)
                stack.append((neighbor, iter(data[neighbor])))
            elif node not in parent or neighbor != parent[node]:
                low[node] = min(low[node], discovered[neighbor])
    return bridges, frozenset(cuts)
