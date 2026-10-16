# Return half-open indices of the shortest subarray with sum at least target.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/min_length_subarray_sum.py)

## Reasoning

Expand a right edge until the running sum reaches the target, then move the left edge forward while the window still qualifies. Nonnegative values make shrinking safe: removing a value cannot hide a shorter qualifying window behind a larger sum.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.min_length_subarray_sum import min_length_subarray_sum

print(repr(min_length_subarray_sum([2, 3, 1, 2, 4, 3], 7)))  # (4, 6)
```

## Boundary to remember

The method requires nonnegative values and a positive target; signed values invalidate the sliding-window argument. It returns half-open indices or None when no range qualifies.

## Practice exercise

Find the shortest span of nonnegative daily counts that reaches a required total.
