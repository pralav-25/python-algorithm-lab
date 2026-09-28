# Group vertices by undirected reachability

[Guide index](../README.md) · [Implementation](../../algorithm_lab/connected_components.py)

## Reasoning

Start a traversal at each still-unvisited vertex and collect everything
reachable from it. Marking discoveries immediately prevents repeated work.
Each collected set is one maximal connected component, including singleton
isolates. The total cost is O(V + E) time and space. This is useful for splitting
an undirected problem into independently processable pieces.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.connected_components import connected_components
>>> graph = {"a": ["b"], "b": ["c"], "remote": [], "x": ["y"]}
>>> groups = connected_components(graph)
>>> set(groups) == {frozenset({"a", "b", "c"}), frozenset({"remote"}), frozenset({"x", "y"})}
True
>>> sum(map(len, groups))
6
>>> connected_components({})
[]

```

## Boundary to remember

Edges are symmetrized even when listed once; neighbor-only vertices are
included. Components follow first-seen vertex order, while vertices inside
each frozenset have no ordering. For mutual reachability that respects edge
direction, use [strongly connected components](strongly_connected_components.md).
