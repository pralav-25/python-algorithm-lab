# Locate edges with no alternate connection

[Guide index](../README.md) · [Implementation](../../algorithm_lab/bridges.py)

## Reasoning

During depth-first search, a child subtree reports the earliest ancestor
it can reach without its parent edge. If that earliest discovery lies strictly
after the parent, the tree edge is the subtree's only connection back. Such an
edge is a bridge. Low-link information finds every bridge in O(V + E) time,
instead of repeatedly removing edges and recomputing connectivity.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.bridges import bridges
>>> graph = {"entry": ["a"], "a": ["b", "c"], "b": ["c"], "island": []}
>>> {frozenset(edge) for edge in bridges(graph)} == {frozenset({"entry", "a"})}
True
>>> bridges({0: [1, 2], 1: [2]})
[]
>>> {frozenset(edge) for edge in bridges({0: [1, 1], 1: [1]})}
{frozenset({0, 1})}

```

## Boundary to remember

This API models a simple undirected graph: duplicate listings are one edge,
not separate parallel connections. Self-loops are ignored. Pair orientation
and result ordering are unspecified, so compare unordered endpoint sets when
checking results. [Articulation points](articulation_points.md) instead model
the loss of a whole vertex.
