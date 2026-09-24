"""Return a directed Euler trail as vertices, or raise ValueError if none exists.

Parallel edges and loops are retained. Zero edges returns [], including graphs
with isolated vertices. Nonzero-degree vertices must belong to one trail;
isolates do not prevent it. O(V+E) time/space. No ordering of valid ties promised.

>>> eulerian_trail({'a': ['b'], 'b': ['a', 'c']})
['b', 'a', 'b', 'c']
"""

from algorithm_lab._graph import normalize_graph


def eulerian_trail(graph):
    data = normalize_graph(graph)
    incoming = dict.fromkeys(data, 0)
    edges = 0
    for neighbors in data.values():
        edges += len(neighbors)
        for v in neighbors:
            incoming[v] += 1
    if not edges:
        return []
    starts, ends = [], []
    for node, neighbors in data.items():
        difference = len(neighbors) - incoming[node]
        if difference == 1:
            starts.append(node)
        elif difference == -1:
            ends.append(node)
        elif difference != 0:
            raise ValueError("incompatible degrees")
    if not (len(starts) == len(ends) == 0 or len(starts) == len(ends) == 1):
        raise ValueError("incompatible degrees")
    start = starts[0] if starts else next(v for v in data if data[v])
    stack, route = [start], []
    while stack:
        if data[stack[-1]]:
            stack.append(data[stack[-1]].pop())
        else:
            route.append(stack.pop())
    if len(route) != edges + 1:
        raise ValueError("edges are disconnected")
    return route[::-1]
