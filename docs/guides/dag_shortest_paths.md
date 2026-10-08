# Settle signed path costs in dependency order

[Guide index](../README.md) · [Implementation](../../algorithm_lab/dag_shortest_paths.py)

## Reasoning

A topological order places every predecessor before its successors. Once
a vertex is processed, all routes that could improve it have already been
considered, so its outgoing edges need only one relaxation pass. This permits
negative weights in O(V + E) time because an acyclic graph cannot contain a
negative cycle. Integer arithmetic preserves exact large costs.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.dag_shortest_paths import dag_shortest_paths
>>> graph = {"start": {"draft": 5, "done": 7}, "draft": {"done": -2}, "unused": {}}
>>> dag_shortest_paths(graph, "start") == {"start": 0, "draft": 5, "done": 3}
True
>>> dag_shortest_paths({"s": {}, "x": {"x": 1}}, "s")
Traceback (most recent call last):
...
ValueError: graph contains a directed cycle

```

## Boundary to remember

Adjacency values are mappings of neighbor to integer weight, unlike the
pair iterables accepted by [Dijkstra](dijkstra.md). Unreachable vertices are
omitted. The source must exist in the normalized graph, and a cycle anywhere
invalidates the input, even when the source cannot reach it.

## Practice exercise

Compute signed costs through a three-stage acyclic workflow and distinguish an unreachable stage from a stage reached at cost zero.

```pycon
>>> from algorithm_lab.dag_shortest_paths import dag_shortest_paths
>>> workflow = {"start": {"review": 4, "ship": 9}, "review": {"ship": -4}, "archive": {}}
>>> costs = dag_shortest_paths(workflow, "start")
>>> costs["ship"], "archive" in costs
(0, False)
>>> assert costs == {"start": 0, "review": 4, "ship": 0}

```

Zero is a legitimate reachable cost after a rebate. Testing dictionary membership distinguishes it from the omitted archive stage; a truthiness check on `costs.get(...)` would confuse those cases.
