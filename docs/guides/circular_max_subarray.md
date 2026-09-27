# Allow a best run to cross the sequence boundary

[Guide index](../README.md) · [Implementation](../../algorithm_lab/circular_max_subarray.py)

## Reasoning

An optimal circular run either stays inside the ordinary linear sequence or wraps around its end. A wrapping run is everything except one contiguous minimum-sum middle slice, so total sum minus that minimum gives the second candidate. Comparing it with the ordinary maximum covers both cases.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.circular_max_subarray import circular_max_subarray
>>> circular_max_subarray([8, -10, 7])
15
>>> values = [4, -1, 2, -5]
>>> brute = max(
...     sum(values[(start + offset) % len(values)] for offset in range(length))
...     for start in range(len(values))
...     for length in range(1, len(values) + 1)
... )
>>> assert circular_max_subarray(values) == brute
>>> circular_max_subarray([-4, -2, -7])
-2

```

## Boundary to remember

A run may use each position at most once. All-negative input needs special handling so removing the entire minimum slice does not incorrectly produce an empty zero-sum answer.
