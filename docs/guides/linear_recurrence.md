# Jump to a distant term of a fixed recurrence

[Guide index](../README.md) · [Implementation](../../algorithm_lab/linear_recurrence.py)

## Reasoning

A vector of recent sequence terms evolves by a companion matrix. Raising that transition matrix to a power skips many repeated recurrence steps while preserving their result. This is useful when the recurrence order is modest and the requested index is much larger than it.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.linear_recurrence import linear_recurrence
>>> linear_recurrence([3], [2], 8)
768
>>> assert linear_recurrence([3], [2], 8) == 3 * 2**8
>>> sequence = [2, 1]
>>> for _ in range(8):
...     sequence.append(3 * sequence[-1] - sequence[-2])
>>> assert linear_recurrence([2, 1], [3, -1], 9) == sequence[9]
>>> linear_recurrence([2, 1], [3, -1], 0)
2

```

## Boundary to remember

Coefficient order is newest preceding term first, while the initial values are given in forward sequence order. Reversing either convention silently describes a different recurrence.
