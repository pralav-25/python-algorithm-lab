"""Return one longest tree path as vertices; empty graph returns [].

Adjacency is symmetrized and duplicate edges collapse. Loops, cycles and
multiple components raise ValueError. O(V+E) time/space. Equal-length ties follow
adjacency traversal order. Labels can be any hashable object.

>>> tree_diameter({0: [1], 1: [2]})
[2, 1, 0]
"""

from collections import deque

from algorithm_lab._graph import normalize_graph


def tree_diameter(graph):
    raw = normalize_graph(graph, undirected=True)
    data = {v: list(dict.fromkeys(rows)) for v, rows in raw.items()}
    if not data:
        return []
    if any(v in rows for v, rows in data.items()) or sum(map(len, data.values())) != 2 * (
        len(data) - 1
    ):
        raise ValueError("graph must be a tree")

    def farthest(start):
        parent, queue = {start: start}, deque([start])
        last = start
        while queue:
            last = queue.popleft()
            for neighbor in data[last]:
                if neighbor not in parent:
                    parent[neighbor] = last
                    queue.append(neighbor)
        return last, parent

    start, visited = farthest(next(iter(data)))
    if len(visited) != len(data):
        raise ValueError("graph must be connected")
    end, parent = farthest(start)
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    return path[::-1]
