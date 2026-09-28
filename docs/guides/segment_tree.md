# Replace individual values and query interval totals

[Guide index](../README.md) · [Implementation](../../algorithm_lab/segment_tree.py)

## Reasoning

Leaves hold values and internal nodes hold sums of their child ranges.
Replacing a leaf updates its ancestors. A range query climbs from both
boundaries, adding only nodes completely contained in the requested interval.
This decomposition gives O(log n) replacements and queries after O(n)
construction, with O(n) storage even when n is not a power of two.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.segment_tree import SegmentTree
>>> tree = SegmentTree([3, -1, 4, 2, 7])
>>> tree.range_sum(1, 4)
5
>>> tree.set(2, 10)
>>> tree.range_sum(1, 4), tree.range_sum(0, len(tree))
(11, 21)
>>> tree.range_sum(5, 5)
0
>>> SegmentTree([]).range_sum(0, 0)
0

```

## Boundary to remember

set replaces a value, unlike [FenwickTree.add](fenwick_tree.md), which
applies a delta. Queries use zero-based half-open ranges, including empty
ranges. Values must be integers, excluding booleans. Invalid indices and
values raise ValueError before any stored totals change.
