# Return (maximum_sum, start_index) among all windows of the requested size.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/max_sum_fixed_window.py)

## Reasoning

Compute the first window once, then slide by subtracting the element that leaves and adding the one that enters. Each shift takes constant work, so scanning every possible fixed-size window is linear.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.max_sum_fixed_window import max_sum_fixed_window

print(repr(max_sum_fixed_window([2, -1, 4, -2, 3], 2)))  # (3, 1)
```

## Boundary to remember

Window size must be between one and the sequence length. Ties choose the earliest start, and negative values are valid because the window size is fixed.

## Practice exercise

Find the best consecutive two-day revenue period and report its earliest starting day when totals tie.
