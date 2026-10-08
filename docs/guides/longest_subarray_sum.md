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

## Practice exercise

Locate the longest target-five budget episode when two equally long episodes are separated by a large cost. Independently verify the earliest-start tie rule.

```pycon
>>> from algorithm_lab.longest_subarray_sum import longest_subarray_sum
>>> costs = [5, 1, -1, 9, 1, -1, 5]
>>> episode = longest_subarray_sum(costs, 5)
>>> episode
(0, 3)
>>> matches = [
...     (start, stop)
...     for start in range(len(costs))
...     for stop in range(start + 1, len(costs) + 1)
...     if sum(costs[start:stop]) == 5
... ]
>>> oracle = min(matches, key=lambda bounds: (-(bounds[1] - bounds[0]), bounds[0]))
>>> assert episode == oracle
>>> assert (4, 7) in matches and sum(costs[episode[0] : episode[1]]) == 5

```

The slices (0, 3) and (4, 7) both have length three and sum five, but the first wins. Keeping the earliest occurrence of a prefix sum preserves the longest candidate for each endpoint. Negative adjustments mean a simple window based on a monotonically growing total would be unreliable.
