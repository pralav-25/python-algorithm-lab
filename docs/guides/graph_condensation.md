# Collapse mutually reachable groups into a DAG

[Guide index](../README.md) · [Implementation](../../algorithm_lab/graph_condensation.py)

## Reasoning

Strongly connected components collect vertices that can all reach each
other. Replacing each component with one vertex removes internal cycles while
preserving connections between groups. Deduplicating those connections produces
a directed acyclic graph in O(V + E) time. This supports dependency analysis
when individual items contain cyclic clusters.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.graph_condensation import graph_condensation
>>> components, dag = graph_condensation({"a": ["b"], "b": ["a", "c", "c"], "c": []})
>>> membership = {v: i for i, group in enumerate(components) for v in group}
>>> membership["a"] == membership["b"]
True
>>> dag[membership["a"]] == frozenset({membership["c"]})
True
>>> dag[membership["c"]]
frozenset()
>>> graph_condensation({})
([], {})

```

## Boundary to remember

Component indices follow the SCC traversal and are not sorted labels.
Use the returned component list to map original vertices back to indices.
Parallel inter-component edges collapse and internal edges disappear. Obtain
an explicit processing order with [topological sort](topological_sort.md).
