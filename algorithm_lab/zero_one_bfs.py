"""Shortest distances in directed graphs with zero-or-one edge costs.

The adjacency mapping stores iterables of (neighbor, weight), where weight
is integer 0 or 1 excluding bool. Vertices are hashable; neighbor-only
vertices are accepted. Return distances for reachable vertices, including
source at distance 0 even if absent. O(V+E) time and storage; all edges are
validated before traversal. A deque schedules zero-cost relaxations first.

>>> zero_one_bfs({'a': [('b', 1), ('c', 0)], 'c': [('b', 0)]}, 'a')
{'a': 0, 'b': 0, 'c': 0}
"""

from collections import deque


def zero_one_bfs(graph, source):
    adjacency = {}
    for vertex, edges in graph.items():
        adjacency[vertex] = []
        for neighbor, weight in edges:
            hash(neighbor)
            if type(weight) is not int or weight not in (0, 1):
                raise ValueError("edge weights must be integer zero or one")
            adjacency[vertex].append((neighbor, weight))
    distances, queue = {source: 0}, deque([(source, 0)])
    while queue:
        vertex, distance = queue.popleft()
        if distances[vertex] != distance:
            continue
        for neighbor, weight in adjacency.get(vertex, ()):
            candidate = distance + weight
            if neighbor not in distances or candidate < distances[neighbor]:
                distances[neighbor] = candidate
                item = (neighbor, candidate)
                if weight:
                    queue.append(item)
                else:
                    queue.appendleft(item)
    return distances
