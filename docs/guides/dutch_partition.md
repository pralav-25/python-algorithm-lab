# Return a three-way partition of integer values around pivot.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/dutch_partition.py)

## Reasoning

Maintain three regions around the current element: values below the pivot, values equal to it, and values above it. A scan advances through the unknown region and swaps each value into the correct side, so every element is classified once.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.dutch_partition import dutch_partition

print(repr(dutch_partition([3, 2, 1, 2, 0], 2)))  # [0, 1, 2, 2, 3]
```

## Boundary to remember

The result groups values but does not sort within a group. All duplicates are preserved and the caller's iterable is copied rather than mutated.

## Practice exercise

Group test scores below, at, and above a pass mark before processing the three bands separately.
