# Group vertices that can mutually reach one another

[Guide index](../README.md) · [Implementation](../../algorithm_lab/strongly_connected_components.py)

## Reasoning

Kosaraju's method first records DFS finishing order. A second traversal
on reversed edges, in reverse finishing order, then isolates each strongly
connected component. Reversing the direction prevents a component search from
escaping into a not-yet-processed component. Both passes are iterative and
use O(V + E) time and space.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.strongly_connected_components import strongly_connected_components
>>> graph = {"a": ["b"], "b": ["a", "c"], "c": ["d"], "d": ["c"], "alone": []}
>>> groups = strongly_connected_components(graph)
>>> set(groups) == {frozenset({"a", "b"}), frozenset({"c", "d"}), frozenset({"alone"})}
True
>>> strongly_connected_components({})
[]
>>> set(strongly_connected_components({"a": ["b"]})) == {frozenset({"a"}), frozenset({"b"})}
True

```

## Boundary to remember

A one-way edge does not merge its endpoints. Singleton components need
no self-loop, and neighbor-only vertices are included. Component ordering is
not an API guarantee, so compare sets when order is irrelevant. Use
[graph condensation](graph_condensation.md) to obtain connections between the
returned groups.
