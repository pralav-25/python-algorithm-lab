# Undo connectivity merges at a saved boundary

[Guide index](../README.md) · [Implementation](../../algorithm_lab/rollback_disjoint_set.py)

## Reasoning

Union by size keeps root paths logarithmic, while a history stack records
each successful merge's changed root and old size. Rolling back pops those
changes in reverse order. Path compression is deliberately absent because it
would introduce extra parent changes to undo. Snapshots take O(1), unions
O(log n), and rollback time is proportional to undone merges.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.rollback_disjoint_set import RollbackDisjointSet
>>> groups = RollbackDisjointSet(4)
>>> groups.union(0, 1)
True
>>> checkpoint = groups.snapshot()
>>> groups.union(1, 2), groups.union(0, 2)
(True, False)
>>> groups.components
2
>>> groups.rollback(checkpoint)
>>> groups.components, groups.find(0) == groups.find(1), groups.find(0) == groups.find(2)
(3, True, False)

```

## Boundary to remember

Tokens are history lengths on the current branch, not persistent version
identifiers. After rollback and new merges, do not reuse tokens from the
discarded branch. Redundant unions add no history. The API supports undoing
recent work, not deleting an arbitrary old connection.
