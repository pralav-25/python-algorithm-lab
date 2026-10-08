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

## Practice exercise

A monitoring network contains two linked pairs and a standalone sensor. Connect the pairs, then check that the standalone sensor still forms its own component.

```pycon
>>> from algorithm_lab.connected_components import connected_components
>>> network = {"a": ["b"], "c": ["d"], "solo": []}
>>> assert len(connected_components(network)) == 3
>>> joined = {"a": ["b"], "b": ["c"], "c": ["d"], "solo": []}
>>> components = set(connected_components(joined))
>>> assert components == {frozenset({"a", "b", "c", "d"}), frozenset({"solo"})}

```

A single cross-component edge merges two groups. Listing the standalone sensor explicitly retains it in the result even though it has no neighbors.
