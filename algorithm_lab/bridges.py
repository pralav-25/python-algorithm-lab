"""Edges whose removal increases the number of connected components.

Treats adjacency as a simple undirected graph: either edge direction suffices,
duplicates collapse, self-loops are ignored. Returns DFS-oriented endpoint pairs
in unspecified order. O(V+E) time and space; no recursion depth limit.

>>> bridges({0: [1], 1: [2, 3], 2: [3]})
[(0, 1)]
"""

from algorithm_lab._undirected_lowlink import lowlink


def bridges(graph):
    return lowlink(graph)[0]
