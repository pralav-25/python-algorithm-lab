"""Return a topological ordering, or raise ValueError if any cycle exists.

Zero-indegree ties follow vertex insertion order, then adjacency order. Neighbor-only
vertices and duplicate edges are supported. Time and space O(V + E).

>>> topological_sort({'plan': ['build'], 'build': ['test']})
['plan', 'build', 'test']
"""

from collections import deque

from algorithm_lab._graph import normalize_graph


def topological_sort(graph):
    data = normalize_graph(graph)
    indegree = dict.fromkeys(data, 0)
    for neighbors in data.values():
        for node in neighbors:
            indegree[node] += 1
    ready = deque(node for node, count in indegree.items() if count == 0)
    result = []
    while ready:
        node = ready.popleft()
        result.append(node)
        for neighbor in data[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                ready.append(neighbor)
    if len(result) != len(data):
        raise ValueError("graph contains a directed cycle")
    return result
