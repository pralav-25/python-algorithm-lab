# Keep both extremes when signs can flip

[Guide index](../README.md) · [Implementation](../../algorithm_lab/max_product_subarray.py)

## Reasoning

Multiplying by a negative value exchanges the roles of the largest and smallest running products. Tracking both extremes ending at each position therefore preserves the candidate that may become a future maximum. A zero naturally resets the running products without needing to divide anything.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.max_product_subarray import max_product_subarray
>>> from math import prod
>>> values = [-3, 2, -5, 0, 4]
>>> max_product_subarray(values)
30
>>> assert max_product_subarray(values) == max(
...     prod(values[i:j]) for i in range(len(values)) for j in range(i + 1, len(values) + 1)
... )
>>> max_product_subarray([-7])
-7

```

## Boundary to remember

The chosen slice is nonempty. Tracking only a positive best-so-far value fails on all-negative singleton inputs and on pairs of negative factors separated by other values.

## Practice exercise

Find the most productive contiguous run when a zero divides the input and
an extra negative factor would turn a good product negative.

```pycon
>>> from algorithm_lab.max_product_subarray import max_product_subarray
>>> from math import prod
>>> factors = [-2, -3, 0, -4, -5, -1]
>>> answer = max_product_subarray(iter(factors))
>>> answer
20
>>> assert answer == prod(factors[3:5])
>>> assert answer > prod(factors[3:])
>>> assert max_product_subarray([0, -2, 0]) == 0

```

The best product after the zero uses two negative factors, not the entire
remaining run. Both running extrema must be updated from the previous
state, because a negative multiplier may promote the old minimum.
