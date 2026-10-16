# Return the smallest positive integer absent from the supplied values.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/smallest_missing_positive.py)

## Reasoning

A positive value x belongs at index x-1 if that index exists. Repeatedly swap each in-range value into its target slot; the first index that does not contain index+1 reveals the missing positive.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.smallest_missing_positive import smallest_missing_positive

print(repr(smallest_missing_positive([3, 4, -1, 1])))  # 2
```

## Boundary to remember

Zero, negative values, and values larger than the list length cannot fill a needed slot. The algorithm works on a copy, preserving the original iterable.

## Practice exercise

Find the first absent positive ticket number in an unsorted list containing duplicates and negative entries.
