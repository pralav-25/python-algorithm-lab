# Answer repeated totals over fixed data

[Guide index](../README.md) · [Implementation](../../algorithm_lab/prefix_sum.py)

## Reasoning

Store the total before every position, including an initial zero. Subtracting the total before the start from the total before the stop cancels everything outside the requested slice. Linear preprocessing then makes each query constant time, which pays off when the underlying observations stay unchanged.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.prefix_sum import PrefixSum
>>> daily = [4, -2, 7, 1]
>>> totals = PrefixSum(daily)
>>> totals.sum(1, 4)
6
>>> assert totals.sum(0, 3) == sum(daily[:3])
>>> daily[1] = 100
>>> totals.sum(1, 2), totals.sum(2, 2)
(-2, 0)

```

## Boundary to remember

The structure is a snapshot. Later edits to the original list do not update its totals; choose a Fenwick or segment tree when updates and queries must be interleaved.
