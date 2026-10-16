# Minimize the absolute difference between sums of two complementary subsets.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/minimum_partition_difference.py)

## Reasoning

Represent reachable subset sums as bits in one integer. For each value, shift the current bitset and union it with itself; the highest reachable sum at or below half the total gives the closest split.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.minimum_partition_difference import minimum_partition_difference

print(repr(minimum_partition_difference([1, 6, 11, 5])))  # 1
```

## Boundary to remember

Values must be nonnegative integers. Every occurrence is assigned to exactly one side, and either side may be empty; the input is copied and left unchanged.

## Practice exercise

Divide nonnegative task durations into two groups with totals as close as possible.
