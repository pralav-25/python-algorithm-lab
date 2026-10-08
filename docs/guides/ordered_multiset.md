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

## Practice exercise

Count values in a half-open score band after adding a score and removing
one duplicate. Use ranks even when a band endpoint is absent.

```pycon
>>> from algorithm_lab.ordered_multiset import OrderedMultiset
>>> scores = OrderedMultiset([12, 7, 12, 5, 20])
>>> scores.add(8)
>>> scores.discard(12)
True
>>> [scores.select(i) for i in range(len(scores))]
[5, 7, 8, 12, 20]
>>> scores.rank(13) - scores.rank(7)
3
>>> assert scores.count(12) == 1
>>> assert scores.select(len(scores) // 2) == 8

```

Subtracting the number strictly below seven from the number strictly
below thirteen counts `[7, 13)`. Neither threshold needs to occur in the
collection, and removing one twelve leaves the other in the band.
