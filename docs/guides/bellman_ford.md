# Relax signed edges and detect reachable negative cycles

[Guide index](../README.md) · [Implementation](../../algorithm_lab/bellman_ford.py)

## Reasoning

Repeated relaxation improves a destination whenever a known route to its
predecessor plus the edge weight is cheaper. Without a reachable negative cycle,
a shortest route needs at most V - 1 edges. An improvement after that many
passes certifies that costs can keep decreasing. The method costs O(VE) time
and permits the negative weights that Dijkstra rejects.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.bellman_ford import bellman_ford
>>> graph = {"s": [("a", 5), ("t", 4)], "a": [("t", -3)], "remote": [("remote", -1)]}
>>> distances = bellman_ford(graph, "s")
>>> distances["t"], distances["remote"]
(2, inf)
>>> bellman_ford({"s": [("s", -1)]}, "s")
Traceback (most recent call last):
...
ValueError: a negative cycle is reachable from the source

```

## Boundary to remember

Unreachable negative cycles do not invalidate distances from this source.
Unreachable vertices have infinite distance. All supplied weights must still be
finite numbers, including weights in disconnected components; booleans are
rejected. [DAG shortest paths](dag_shortest_paths.md) offers linear time when
the entire graph is acyclic.
