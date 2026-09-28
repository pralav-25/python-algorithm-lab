# Track sorted values with duplicate-aware ranks

[Guide index](../README.md) · [Implementation](../../algorithm_lab/ordered_multiset.py)

## Reasoning

A sorted list makes selection by rank direct and lets binary search find
both boundaries of a repeated value. The left boundary counts strictly smaller
items; the gap between boundaries counts equal items. Rank and count take
O(log n), selection O(1), and insertion or removal O(n) because the list may
need to shift entries.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.ordered_multiset import OrderedMultiset
>>> scores = OrderedMultiset([8, 3, 8, 1])
>>> scores.rank(8), scores.count(8), scores.select(2)
(2, 2, 8)
>>> scores.discard(8), scores.count(8)
(True, 1)
>>> scores.add(4)
>>> [scores.select(i) for i in range(len(scores))]
[1, 3, 4, 8]
>>> scores.discard(99)
False

```

## Boundary to remember

discard removes one copy rather than all equal values. select uses
nonnegative zero-based indices and rejects negative indexing. Values need a
consistent total order. This implementation favors simplicity; frequent
updates to a very large collection still cost linear time.
