# Connect all vertices with minimum total edge weight

[Guide index](../README.md) · [Implementation](../../algorithm_lab/minimum_spanning_tree.py)

## Reasoning

Kruskal's algorithm considers edges from lightest to heaviest, accepting
an edge only when its endpoints belong to different components. This avoids
cycles while joining components through a cheapest available edge. Sorting
dominates the O(E log E + V) cost. A connected nonempty result has V - 1 edges,
which can be checked alongside its reported total weight.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.minimum_spanning_tree import minimum_spanning_tree
>>> roads = [(0, 1, 6), (1, 2, 1), (0, 2, 3), (2, 3, -1)]
>>> total, selected = minimum_spanning_tree(4, roads)
>>> total, selected
(3, [(2, 3, -1), (1, 2, 1), (0, 2, 3)])
>>> sum(weight for _, _, weight in selected) == total
True
>>> minimum_spanning_tree(3, [(0, 1, 2)], require_connected=False)
(2, [(0, 1, 2)])

```

## Boundary to remember

Vertices are indices 0 through V - 1. Negative weights and parallel edges
are allowed; self-loops cannot help and are ignored after validation. A
disconnected nonempty graph raises ValueError unless a spanning forest is
requested. Equal weights retain input order.

## Practice exercise

Build a minimum spanning forest for two disconnected groups, including
a self-loop and parallel edges that should not enter the result.

```pycon
>>> from algorithm_lab.minimum_spanning_tree import minimum_spanning_tree
>>> links = [(0, 0, -10), (0, 1, 5), (0, 1, 2), (1, 2, 3), (0, 2, 8), (3, 4, 1)]
>>> total, forest = minimum_spanning_tree(5, links, require_connected=False)
>>> total, forest
(6, [(3, 4, 1), (0, 1, 2), (1, 2, 3)])
>>> assert len(forest) == 5 - 2
>>> assert all(first != second for first, second, weight in forest)
>>> assert sum(weight for first, second, weight in forest) == total

```

A negative self-loop still cannot connect different components. The
lighter parallel edge wins, and a forest with two components has two
fewer edges than vertices; requiring connectivity would reject this graph.
