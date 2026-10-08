# Find single vertices that disconnect a network

[Guide index](../README.md) · [Implementation](../../algorithm_lab/articulation_points.py)

## Reasoning

A depth-first search records when each vertex is discovered and the earliest
ancestor reachable from each child subtree. If a child cannot reach above its
parent, removing that parent separates the child. The DFS root is special: it
needs at least two child subtrees to be an articulation point. This identifies
single points of failure in O(V + E) time without removing every vertex.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.articulation_points import articulation_points
>>> network = {"hub": ["a", "b"], "a": ["b"], "b": ["tail"], "isolated": []}
>>> articulation_points(network) == frozenset({"b"})
True
>>> articulation_points({"hub": ["a", "b"]}) == frozenset({"hub"})
True
>>> articulation_points({"only": ["only"]})
frozenset()

```

## Boundary to remember

Edges are treated as undirected even when listed in one direction. Repeated
edges collapse and self-loops are ignored. Removing an isolated vertex reduces
the component count, so it is not an articulation point. Compare this with
[bridges](bridges.md), which identify critical edges instead of vertices.

## Practice exercise

A four-station line has two single-station failure points. Determine how adding a connection between its endpoints changes the failure analysis.

```pycon
>>> from algorithm_lab.articulation_points import articulation_points
>>> line = {0: [1], 1: [2], 2: [3]}
>>> assert articulation_points(line) == frozenset({1, 2})
>>> redundant = {0: [1, 3], 1: [2], 2: [3]}
>>> articulation_points(redundant)
frozenset()

```

The added edge makes a cycle. Removing any one station leaves a connected path through the other three, so the redundant network has no articulation point.
