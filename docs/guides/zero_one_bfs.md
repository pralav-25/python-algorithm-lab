# Prioritize free edges with a double-ended queue

[Guide index](../README.md) · [Implementation](../../algorithm_lab/zero_one_bfs.py)

## Reasoning

When every edge costs zero or one, a full priority queue is unnecessary.
A zero-cost improvement goes to the front of a deque, while a one-cost
improvement goes to the back. This preserves distance-layer processing and
lets cheaper rediscoveries replace earlier tentative costs. Stale queued
entries are skipped, giving O(V + E) time and space.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.zero_one_bfs import zero_one_bfs
>>> graph = {"s": [("t", 1), ("a", 0)], "a": [("t", 0)], "t": [("u", 1)], "island": []}
>>> zero_one_bfs(graph, "s") == {"s": 0, "t": 0, "a": 0, "u": 1}
True
>>> zero_one_bfs({}, "alone")
{'alone': 0}
>>> zero_one_bfs({"s": [("t", True)]}, "s")
Traceback (most recent call last):
...
ValueError: edge weights must be integer zero or one

```

## Boundary to remember

Weights must be the integers 0 or 1; floats and booleans are rejected.
All edges are validated, even disconnected ones. Unreachable vertices are
omitted, and a missing source is isolated at distance zero. Ordinary BFS would
minimize edge count and can miss a longer route with a lower zero-one cost.
