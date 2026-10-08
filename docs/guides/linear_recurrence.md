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

## Practice exercise

Count ways to climb seven steps using jumps of one, two, or three. Verify the recurrence result by enumerating every possible jump sequence.

```pycon
>>> from itertools import product
>>> from algorithm_lab.linear_recurrence import linear_recurrence
>>> ways = linear_recurrence([1, 1, 2], [1, 1, 1], 7)
>>> ways
44
>>> enumerated = sum(
...     sum(jumps) == 7 for length in range(8) for jumps in product((1, 2, 3), repeat=length)
... )
>>> assert ways == enumerated

```

Classifying a route by its last jump gives the sum of the previous three counts. Heights zero, one, and two have one, one, and two routes respectively, including the empty route at zero. The exhaustive check counts ordered jump sequences, so (1, 2) and (2, 1) remain distinct.
