"""Return a vertex-to-0/1 coloring, or None if the graph is not bipartite.

Listed edges are interpreted as undirected. Self-loops fail. Isolated vertices
are retained, and each component's first-seen vertex gets color 0. Time/space O(V + E).

>>> bipartite_coloring({0: [1], 1: [2]})
{0: 0, 1: 1, 2: 0}
>>> bipartite_coloring({0: [1, 2], 1: [2]}) is None
True
"""

from collections import deque

from algorithm_lab._graph import normalize_graph


def bipartite_coloring(graph):
    data = normalize_graph(graph, undirected=True)
    colors = {}
    for start in data:
        if start in colors:
            continue
        queue = deque([start])
        colors[start] = 0
        while queue:
            node = queue.popleft()
            for neighbor in data[node]:
                if neighbor not in colors:
                    colors[neighbor] = 1 - colors[node]
                    queue.append(neighbor)
                elif colors[neighbor] == colors[node]:
                    return None
    return colors
