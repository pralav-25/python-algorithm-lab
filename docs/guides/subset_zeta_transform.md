# Aggregate a value over every subset of a mask

[Guide index](../README.md) · [Implementation](../../algorithm_lab/subset_zeta_transform.py)

## Reasoning

For each bit, add the total for masks without that bit into corresponding masks with it. After processing a set of bits, each entry includes all ways to remove those processed bits. Repeating for all bits aggregates every subset in n log n operations rather than enumerating subsets separately for each mask.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.subset_zeta_transform import subset_zeta_transform
>>> values = [2, 3, 5, 7]
>>> totals = subset_zeta_transform(values)
>>> totals
[2, 5, 7, 17]
>>> assert all(
...     totals[mask] == sum(value for sub, value in enumerate(values) if sub & mask == sub)
...     for mask in range(4)
... )
>>> assert values == [2, 3, 5, 7]

```

## Boundary to remember

The array length must be a nonzero power of two. Its indices are bit masks, so index order carries the set structure; this is not an ordinary prefix sum.
