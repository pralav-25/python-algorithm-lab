"""Map each vertex to the frozenset it can reach in a directed graph.

With reflexive=True (default), every node reaches itself. Otherwise self is
included only if a nonempty path cycles back. Neighbor-only vertices are retained.
O(V*(V+E)) time and O(V²+E) space; hashable labels, no recursion.

>>> transitive_closure({0: [1], 1: [2]}, reflexive=False)
{0: frozenset({1, 2}), 1: frozenset({2}), 2: frozenset()}
"""

from algorithm_lab._graph import normalize_graph


def transitive_closure(graph, *, reflexive=True):
    data = normalize_graph(graph)
    result = {}
    for source in data:
        seen = {source} if reflexive else set()
        stack = list(data[source])
        while stack:
            node = stack.pop()
            if node not in seen:
                seen.add(node)
                stack.extend(data[node])
        result[source] = frozenset(seen)
    return result
