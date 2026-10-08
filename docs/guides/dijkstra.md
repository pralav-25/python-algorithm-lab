# Expand the cheapest unsettled route first

[Guide index](../README.md) · [Implementation](../../algorithm_lab/dijkstra.py)

## Reasoning

A min-heap selects the smallest known tentative distance. Nonnegative
edge weights ensure that a longer route cannot later become cheaper by taking
another edge. Relaxations add improved heap entries; stale entries are skipped
when popped. The implementation uses O((V + E) log(V + E)) time and an insertion
counter so tied costs never require comparing vertex labels.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.dijkstra import dijkstra
>>> graph = {"s": [("t", 9), ("via", 2)], "via": [("t", 3)], "island": []}
>>> distances = dijkstra(graph, "s")
>>> distances["t"], distances["island"]
(5, inf)
>>> dijkstra({}, "s")
{'s': 0}
>>> dijkstra({"s": [("t", -1)]}, "s")
Traceback (most recent call last):
...
ValueError: weights must be nonnegative

```

## Boundary to remember

Weights must be finite nonnegative integers or floats, excluding booleans.
All edges are checked, including disconnected ones. The return value contains
distances rather than predecessor paths. For signed weights use
[Bellman-Ford](bellman_ford.md), or the faster DAG-specific routine when applicable.

## Practice exercise

A toll-free connection makes a three-step route cheaper than a direct toll road. Verify distances when a later relaxation replaces an earlier heap entry.

```pycon
>>> from algorithm_lab.dijkstra import dijkstra
>>> roads = {"s": [("t", 20), ("a", 3)], "a": [("b", 0)], "b": [("t", 2)]}
>>> distances = dijkstra(roads, "s")
>>> distances["a"], distances["b"], distances["t"]
(3, 3, 5)
>>> assert distances["t"] == 3 + 0 + 2

```

Zero-cost edges satisfy Dijkstra's nonnegative-weight requirement. The twenty-unit entry for the destination becomes stale after the five-unit route is found; a stale heap entry must never overwrite the improved distance.
