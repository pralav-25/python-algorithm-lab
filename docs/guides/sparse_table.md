# Precompute overlapping blocks for constant-time minima

[Guide index](../README.md) · [Implementation](../../algorithm_lab/sparse_table.py)

## Reasoning

Store minima for every interval length that is a power of two. Any query
can be covered by two such blocks chosen from its left and right endpoints.
Their overlap does not matter because taking a minimum twice changes nothing.
O(n log n) preprocessing and storage then support O(1) minimum queries on
fixed data.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.sparse_table import SparseTable
>>> readings = [8, 3, 6, 1, 9, 2]
>>> table = SparseTable(readings)
>>> table.query(0, 3), table.query(1, 6), table.query(4, 5)
(3, 1, 9)
>>> readings[3] = 100
>>> table.query(0, 6)
1
>>> table.query(2, 2)
Traceback (most recent call last):
...
ValueError: range must be nonempty

```

## Boundary to remember

Ranges are half-open and must be nonempty. The input is copied at
construction, and there is no update API. This overlapping-block trick works
for idempotent operations such as minimum; using ordinary sums would double
count the overlap. Values require a consistent total order.
