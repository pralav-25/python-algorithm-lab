# Recover the fewest-edge route through a directed graph

[Guide index](../README.md) · [Implementation](../../algorithm_lab/bfs_shortest_path.py)

## Reasoning

Breadth-first search visits vertices in layers of increasing edge count.
The first discovery of a vertex therefore gives a shortest route to it.
Recording just one predecessor per vertex lets the search reconstruct a route
without keeping every partial path. An adjacency snapshot and a queue give
O(V + E) time and space, including support for one-pass neighbor iterators.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.bfs_shortest_path import bfs_shortest_path
>>> routes = {"home": ["park", "shop"], "park": ["office"], "shop": ["office"]}
>>> bfs_shortest_path(routes, "home", "office")
['home', 'park', 'office']
>>> bfs_shortest_path(routes, "office", "home") is None
True
>>> bfs_shortest_path({}, "here", "here")
['here']

```

## Boundary to remember

Edges remain directed. Adjacency order chooses between equally short routes,
and a vertex appearing only as a neighbor is still usable. The result minimizes
edge count, not a weighted cost; use [Dijkstra](dijkstra.md) for nonnegative
weighted edges.
