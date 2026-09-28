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
