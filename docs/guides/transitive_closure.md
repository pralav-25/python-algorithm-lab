# Precompute which destinations every vertex can reach

[Guide index](../README.md) · [Implementation](../../algorithm_lab/transitive_closure.py)

## Reasoning

Traverse outward from each source and retain every discovered vertex.
The resulting lookup table answers reachability queries without another graph
search. Repeating traversal gives O(V(V + E)) time, with up to O(V squared)
stored reachability entries plus the adjacency snapshot. Whether zero-edge
paths count is controlled explicitly by the reflexive option.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.transitive_closure import transitive_closure
>>> graph = {"a": ["b"], "b": ["a", "c"]}
>>> reach = transitive_closure(graph, reflexive=False)
>>> reach["a"] == frozenset({"a", "b", "c"})
True
>>> reach["c"]
frozenset()
>>> transitive_closure(graph)["c"] == frozenset({"c"})
True

```

## Boundary to remember

With reflexive=False, a vertex still reaches itself if a nonempty cycle
returns to it. With the default True, every vertex reaches itself even when
isolated. Neighbor-only vertices become keys. This records reachability, not
shortest distance or the path that proves a connection.
