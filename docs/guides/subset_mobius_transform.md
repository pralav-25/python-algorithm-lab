# Recover exact mask values from subset totals

[Guide index](../README.md) · [Implementation](../../algorithm_lab/subset_mobius_transform.py)

## Reasoning

The subset zeta transform adds lower-mask contributions along each bit dimension. Replacing those additions with subtractions reverses the process. This inversion separates a mask’s own value from the totals contributed by all its proper subsets.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.subset_mobius_transform import subset_mobius_transform
>>> from algorithm_lab.subset_zeta_transform import subset_zeta_transform
>>> subset_mobius_transform([2, 5, 7, 17])
[2, 3, 5, 7]
>>> values = [-2, 0, 4, -1, 5, 2, 0, 3]
>>> assert subset_mobius_transform(subset_zeta_transform(values)) == values
>>> subset_mobius_transform([9])
[9]

```

## Boundary to remember

These inputs are subset totals indexed by masks, not ordinary cumulative totals indexed along a line. Negative recovered values are valid integer results.
