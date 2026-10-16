# Return unique sorted 4-tuples summing to target, in lexicographic order.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/four_sum.py)

## Reasoning

Sort a copy, fix two values, and use inward-moving pointers for the remaining pair. When a sum is too small or large, one pointer moves in a direction that cannot discard a valid solution; skipping equal values removes duplicate tuples.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.four_sum import four_sum

print(repr(four_sum([1, 0, -1, 0, -2, 2])))  # [(-2, -1, 1, 2), (-2, 0, 0, 2), (-1, 0, 0, 1)]
```

## Boundary to remember

Each answer uses four distinct input positions, even when values repeat. Results are unique, sorted internally, and returned in lexicographic order.

## Practice exercise

Find unique four-item combinations that exactly meet a target budget while keeping the original list unchanged.
