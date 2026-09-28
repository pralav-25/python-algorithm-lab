# Choose a vertex that balances the remaining components

[Guide index](../README.md) · [Implementation](../../algorithm_lab/tree_centroids.py)

## Reasoning

Root the tree and accumulate subtree sizes from leaves upward. Removing
a vertex leaves one component per child subtree and, unless it is the root,
one component containing the rest of the tree. A centroid is a vertex for which
none of these components exceeds half the total size. This finds the one or
two centroids in O(V + E) time.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.tree_centroids import tree_centroids
>>> tree_centroids({0: [1], 1: [2], 2: [3]})
[1, 2]
>>> tree_centroids({"hub": ["a", "b", "c", "d"]})
['hub']
>>> tree_centroids({"only": []})
['only']
>>> tree_centroids({})
[]

```

## Boundary to remember

Adjacency is symmetrized and duplicate edges collapse, but cycles,
self-loops, and disconnected input raise ValueError. Centroids balance
component sizes; they need not coincide with tree centers, which minimize
maximum distance. Returned centroids follow normalized graph order.
