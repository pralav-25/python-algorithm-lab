"""Visit reachable vertices in depth-first preorder, following adjacency order.

Repeated edges and cycles visit each vertex once. A missing start is an isolated
vertex. Time and space O(V + E); vertices may be any hashable value.

>>> depth_first_search({'a': ['b', 'c'], 'b': ['c', 'd']}, 'a')
['a', 'b', 'c', 'd']
"""

from algorithm_lab._graph import normalize_graph


def depth_first_search(graph, start):
    data = normalize_graph(graph)
    stack, visited, result = [start], set(), []
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        result.append(node)
        stack.extend(reversed(data.get(node, [])))
    return result
