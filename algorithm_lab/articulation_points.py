"""Return a frozenset of vertices whose removal increases component count.

O(V+E) time/space, iterative DFS. Uses simple undirected semantics: asymmetric
edges are symmetrized, duplicate edges collapse, loops are ignored. Isolates
are included in analysis but are not articulation points.

>>> articulation_points({0: [1], 1: [2, 3]}) == frozenset({1})
True
"""

from algorithm_lab._undirected_lowlink import lowlink


def articulation_points(graph):
    return lowlink(graph)[1]
