# Adjust measurements while keeping fast prefix totals

[Guide index](../README.md) · [Implementation](../../algorithm_lab/fenwick_tree.py)

## Reasoning

A Fenwick tree stores totals for overlapping blocks whose lengths are
determined by the lowest set bit of each internal index. A prefix query visits
disjoint blocks; a point update visits exactly the blocks containing that point.
Subtracting two prefix totals answers any half-open range. Construction is
O(n), and both updates and queries take O(log n) time.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.fenwick_tree import FenwickTree
>>> tree = FenwickTree([4, -2, 7, 1])
>>> tree.prefix_sum(3), tree.range_sum(1, 4)
(9, 6)
>>> tree.add(1, 5)
>>> tree.range_sum(1, 4), tree.range_sum(2, 2)
(11, 0)
>>> FenwickTree([]).prefix_sum(0)
0

```

## Boundary to remember

Public indices are zero-based, and stop is excluded from a query. add
applies a delta rather than replacing the old value. Values and deltas must
be integers, excluding booleans. For a replacement API compare
[segment trees](segment_tree.md); for immutable data compare prefix sums.
