# Count every target-sum slice, including overlapping ones

[Guide index](../README.md) · [Implementation](../../algorithm_lab/subarray_sum_count.py)

## Reasoning

At each endpoint, every earlier prefix sum equal to current_prefix minus target begins a matching slice. A frequency map counts all such starts instead of keeping just one index. Recording the current prefix after counting prevents accidentally including an empty slice when the target is zero.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.subarray_sum_count import subarray_sum_count
>>> values, target = [1, -1, 1, -1], 0
>>> subarray_sum_count(values, target)
4
>>> brute = sum(sum(values[start:stop]) == target for start in range(len(values)) for stop in range(start+1, len(values)+1))
>>> assert subarray_sum_count(values, target) == brute
>>> subarray_sum_count([0, 0], 0)
3

```

## Boundary to remember

Repeated prefixes and negative values are meaningful. A sliding window based on monotonic sums would fail when negative entries let the sum decrease.
