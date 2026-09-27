# Find a longest target-sum slice with signed values

[Guide index](../README.md) · [Implementation](../../algorithm_lab/longest_subarray_sum.py)

## Reasoning

Two prefix sums differ by the total between their positions. At each endpoint, look for an earlier prefix equal to the current prefix minus the target. Keeping the earliest occurrence of each prefix maximizes the resulting slice length. This works with negative numbers, unlike a window that assumes sums only grow.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.longest_subarray_sum import longest_subarray_sum
>>> values = [2, -2, 3, 1, -1]
>>> start, stop = longest_subarray_sum(values, 3)
>>> start, stop, sum(values[start:stop])
(0, 5, 3)
>>> longest_subarray_sum([1, 2], 0) is None
True
>>> longest_subarray_sum([0, 0], 0)
(0, 2)

```

## Boundary to remember

The result is a nonempty half-open slice. For target zero, a missing match is still None rather than an empty slice; repeated zero prefixes are useful because they can extend a real solution.
