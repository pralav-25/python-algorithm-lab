"""Return a shortest directed path, or None if the goal is unreachable.

Vertices are arbitrary hashable values; adjacency order resolves ties. Missing
vertices are isolated. Neighbor-only vertices are included. Time and space
O(V + E), including an input snapshot so neighbor iterators are supported.

>>> bfs_shortest_path({'a': ['b', 'c'], 'b': ['d'], 'c': ['d']}, 'a', 'd')
['a', 'b', 'd']
"""

from collections import deque
from collections.abc import Hashable, Iterable, Mapping

from algorithm_lab._graph import normalize_graph


def bfs_shortest_path(graph: Mapping[Hashable, Iterable[Hashable]], start, goal):
    data = normalize_graph(graph)
    queue, parents = deque([start]), {start: start}
    while queue:
        node = queue.popleft()
        if node == goal:
            path = [node]
            while node != start:
                node = parents[node]
                path.append(node)
            return path[::-1]
        for neighbor in data.get(node, []):
            if neighbor not in parents:
                parents[neighbor] = node
                queue.append(neighbor)
    return None
