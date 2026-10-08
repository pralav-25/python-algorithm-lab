# Find the nearest starting point in one traversal

[Guide index](../README.md) · [Implementation](../../algorithm_lab/multi_source_bfs.py)

## Reasoning

Initialize every source at distance zero before processing the queue.
The usual breadth-first layers then represent distance from the nearest source,
so separate traversals are unnecessary. Each reachable vertex is discovered
once. Including normalization and source iteration, time and space are
O(V + E + S), where S is the number of supplied sources.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.multi_source_bfs import multi_source_bfs
>>> graph = {"north": ["a"], "a": ["b"], "south": ["b"], "b": ["c"], "island": []}
>>> distances = multi_source_bfs(graph, ["north", "south", "north"])
>>> distances == {"north": 0, "south": 0, "a": 1, "b": 1, "c": 2}
True
>>> multi_source_bfs(graph, [])
{}
>>> multi_source_bfs({}, ["outside"])
{'outside': 0}

```

## Boundary to remember

Edges are directed and distances count edges. Repeated sources are
deduplicated; missing sources behave as isolated vertices. Unreachable
vertices are omitted rather than assigned infinity. The result gives nearest
distances but does not identify which source attained them.

## Practice exercise

Measure delivery distance from either depot in a directed network with
a cycle and a vertex that can reach a depot but cannot be reached from it.

```pycon
>>> from algorithm_lab.multi_source_bfs import multi_source_bfs
>>> roads = {
...     "west": ["junction"],
...     "east": ["market"],
...     "junction": ["market", "center"],
...     "market": ["center"],
...     "center": ["shop"],
...     "shop": ["junction"],
...     "closed": ["west"],
... }
>>> distances = multi_source_bfs(roads, ["west", "east"])
>>> assert distances == {"west": 0, "east": 0, "junction": 1, "market": 1, "center": 2, "shop": 3}
>>> assert "closed" not in distances
>>> assert all(
...     distances[neighbor] <= distances[node] + 1 for node in distances for neighbor in roads[node]
... )

```

All depots must enter the initial queue at distance zero. The cycle does
not create shorter revisits, and reversing the edge from `closed` would
change reachability: directed distance follows the supplied orientation.
