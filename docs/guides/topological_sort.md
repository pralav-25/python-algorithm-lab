# Schedule every dependency before its dependents

[Guide index](../README.md) · [Implementation](../../algorithm_lab/topological_sort.py)

## Reasoning

Count incoming edges, then queue vertices with no remaining prerequisites.
Emitting a vertex removes its outgoing dependencies; newly ready vertices join
the queue. If some vertices never become ready, a directed cycle exists.
Kahn's algorithm takes O(V + E) time and includes isolated work items and
vertices that appear only as neighbors.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.topological_sort import topological_sort
>>> graph = {"plan": ["build", "review"], "build": ["ship"], "review": ["ship"]}
>>> order = topological_sort(graph)
>>> order
['plan', 'build', 'review', 'ship']
>>> positions = {node: i for i, node in enumerate(order)}
>>> all(positions[a] < positions[b] for a, neighbors in graph.items() for b in neighbors)
True
>>> topological_sort({"x": ["x"]})
Traceback (most recent call last):
...
ValueError: graph contains a directed cycle

```

## Boundary to remember

Here a -> b means a must precede b. Duplicate edge listings are supported:
each increases and later decreases indegree. Ready-vertex ties follow insertion
and adjacency order, not alphabetical sorting. A cycle in any component rejects
the whole graph; use a cycle witness to investigate it.
