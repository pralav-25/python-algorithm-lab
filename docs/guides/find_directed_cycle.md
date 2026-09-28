# Return a concrete witness of cyclic dependencies

[Guide index](../README.md) · [Implementation](../../algorithm_lab/find_directed_cycle.py)

## Reasoning

DFS distinguishes vertices still on the active search path from vertices
whose exploration is complete. An edge to an active vertex closes a cycle;
parent pointers reconstruct the witness. An edge to a completed vertex is
harmless. Explicit iterator frames keep the traversal iterative, using
O(V + E) time and space.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.find_directed_cycle import find_directed_cycle
>>> graph = {"a": ["b"], "b": ["c"], "c": ["a", "done"]}
>>> cycle = find_directed_cycle(graph)
>>> cycle
['a', 'b', 'c', 'a']
>>> all(b in graph[a] for a, b in zip(cycle, cycle[1:]))
True
>>> find_directed_cycle({"a": ["b", "c"], "b": ["c"]})
[]
>>> find_directed_cycle({"self": ["self"]})
['self', 'self']

```

## Boundary to remember

The first vertex is repeated at the end so every consecutive pair is a
cycle edge. An empty list means no cycle anywhere in the graph, including
disconnected components. Adjacency order selects the first witness; the result
does not enumerate all cycles.
