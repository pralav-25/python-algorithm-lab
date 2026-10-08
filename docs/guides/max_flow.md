# Increase network throughput through residual routes

[Guide index](../README.md) · [Implementation](../../algorithm_lab/max_flow.py)

## Reasoning

A residual graph records how much additional flow each edge can carry
and how much previous flow can be undone. Breadth-first searches find
augmenting paths; pushing each path's bottleneck capacity increases total
throughput. Reverse residual edges allow earlier choices to be corrected.
Edmonds-Karp takes O(V E squared) time and O(V + E) space.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.max_flow import max_flow
>>> graph = {"s": {"a": 3, "b": 2}, "a": {"t": 2}, "b": {"t": 2}}
>>> value, source_side = max_flow(graph, "s", "t")
>>> value
4
>>> source_side == frozenset({"s", "a"})
True
>>> sum(capacity for a in source_side for b, capacity in graph[a].items() if b not in source_side)
4

```

## Boundary to remember

The returned cut contains vertices reachable from the source in the final
residual graph. Its outgoing capacity in the original graph certifies the
maximum flow. Capacities are nonnegative integers; source and sink must be
distinct existing vertices. The API returns a total and cut, not per-edge flows.

## Practice exercise

Route two unit jobs through two shared servers, even when the first chosen
route must later be undone. Check both the throughput and its cut certificate.

```pycon
>>> from algorithm_lab.max_flow import max_flow
>>> network = {
...     "s": {"a": 1, "b": 1},
...     "a": {"x": 1, "y": 1},
...     "b": {"x": 1},
...     "x": {"t": 1},
...     "y": {"t": 1},
...     "t": {},
... }
>>> before = {node: dict(edges) for node, edges in network.items()}
>>> throughput, cut = max_flow(network, "s", "t")
>>> throughput, cut == frozenset({"s"})
(2, True)
>>> assert (
...     sum(cap for node in cut for neighbor, cap in network[node].items() if neighbor not in cut)
...     == throughput
... )
>>> assert network == before

```

Sending `a` to `x` first leaves `b` blocked. The residual route can cancel
that choice and send `a` to `y`; a method that only consumes forward
capacities would miss this second unit of flow.
