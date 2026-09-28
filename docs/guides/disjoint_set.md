# Merge connectivity groups without enumerating them

[Guide index](../README.md) · [Implementation](../../algorithm_lab/disjoint_set.py)

## Reasoning

Each vertex points toward a representative root. Union by size attaches
the smaller tree to the larger one, while path compression shortens routes
during find operations. A successful union reduces the component count once;
repeating an existing connection does nothing. After O(n) initialization,
find and union take amortized O(alpha(n)) time.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.disjoint_set import DisjointSet
>>> groups = DisjointSet(5)
>>> groups.union(0, 1), groups.union(1, 2), groups.union(2, 0)
(True, True, False)
>>> groups.components, groups.component_size(0), groups.connected(0, 2)
(3, 3, True)
>>> set(groups.groups()) == {frozenset({0, 1, 2}), frozenset({3}), frozenset({4})}
True

```

## Boundary to remember

Vertices are integer indices from 0 through n - 1, excluding booleans.
Representative identities are an implementation choice; compare connectivity
or groups instead of expecting a particular root. Connections cannot be
deleted here. [Rollback disjoint sets](rollback_disjoint_set.md) support undoing
recent merges.
