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

## Practice exercise

Check a release workflow whose shipping chain is acyclic but whose disconnected audit tasks depend on each other. Return and validate the audit cycle, then remove its closing edge.

```pycon
>>> from algorithm_lab.find_directed_cycle import find_directed_cycle
>>> workflow = {"prepare": ["ship"], "ship": [], "audit": ["review"], "review": ["audit"]}
>>> witness = find_directed_cycle(workflow)
>>> witness
['audit', 'review', 'audit']
>>> assert witness[0] == witness[-1]
>>> assert all(target in workflow[source] for source, target in zip(witness, witness[1:]))
>>> workflow["review"] = []
>>> find_directed_cycle(workflow)
[]

```

A search confined to the shipping tasks would miss this defect. The outer traversal starts a new DFS in every unexplored component, while the repeated endpoint makes the returned list a checkable closed walk.
