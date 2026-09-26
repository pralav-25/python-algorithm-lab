"""Shortest directed distances from any of several sources using one BFS.

Return a distance mapping containing only reachable vertices. Sources absent from
the graph are isolated, repeated sources count once, and empty sources yield {}.
Hashable labels and neighbor iterators are supported; input order resolves visit
ties. O(V + E + S) time and space including the graph snapshot.

>>> multi_source_bfs({'a': ['b'], 'c': ['d'], 'b': ['d']}, ['a', 'c'])
{'a': 0, 'c': 0, 'b': 1, 'd': 1}
"""

from collections import deque

from algorithm_lab._graph import normalize_graph


def multi_source_bfs(graph, sources):
    data = normalize_graph(graph)
    distances = dict.fromkeys(sources, 0)
    queue = deque(distances)
    while queue:
        node = queue.popleft()
        for neighbor in data.get(node, ()):
            if neighbor not in distances:
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)
    return distances
