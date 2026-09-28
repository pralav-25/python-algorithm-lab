# Split a network into two conflict-free sides

[Guide index](../README.md) · [Implementation](../../algorithm_lab/bipartite_coloring.py)

## Reasoning

Assign the first vertex of each component color 0, then propagate the
opposite color across every edge. A conflict means an odd cycle prevents any
two-coloring. Each vertex and edge is processed a constant number of times,
giving O(V + E) time. This can check whether pairwise incompatibilities admit
two groups before constructing a matching.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.bipartite_coloring import bipartite_coloring
>>> colors = bipartite_coloring({"a": ["b", "d"], "b": ["c"], "c": ["d"], "alone": []})
>>> colors["a"] == colors["c"] and colors["b"] == colors["d"]
True
>>> colors["a"] != colors["b"] and colors["alone"] == 0
True
>>> bipartite_coloring({0: [1, 2], 1: [2]}) is None
True
>>> bipartite_coloring({0: [0]}) is None
True

```

## Boundary to remember

Listed edges are interpreted as undirected. A self-loop is already a
conflict. Each disconnected component starts independently, so color numbers
across components do not imply any relationship. None denotes failure; an
empty dictionary is the valid coloring of an empty graph.
