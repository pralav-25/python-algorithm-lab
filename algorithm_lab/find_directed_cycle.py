"""Return a directed cycle with its first vertex repeated at the end, or [].

O(V+E) time/space. Neighbor-only nodes and self-loops are supported. The first
cycle encountered by adjacency-order DFS is returned; input is unchanged.

>>> find_directed_cycle({0: [1], 1: [2], 2: [0]})
[0, 1, 2, 0]
"""

from algorithm_lab._graph import normalize_graph


def find_directed_cycle(graph):
    data = normalize_graph(graph)
    color, parent = {}, {}
    for root in data:
        if root in color:
            continue
        color[root] = 1
        stack = [(root, iter(data[root]))]
        while stack:
            node, neighbors = stack[-1]
            try:
                neighbor = next(neighbors)
            except StopIteration:
                color[node] = 2
                stack.pop()
                continue
            if neighbor not in color:
                color[neighbor], parent[neighbor] = 1, node
                stack.append((neighbor, iter(data[neighbor])))
            elif color[neighbor] == 1:
                cycle = [node]
                while cycle[-1] != neighbor:
                    cycle.append(parent[cycle[-1]])
                return cycle[::-1] + [neighbor]
    return []
