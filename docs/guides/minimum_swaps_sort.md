# Return the minimum number of arbitrary pair swaps to sort distinct integers.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/minimum_swaps_sort.py)

## Reasoning

Map each distinct value to its sorted destination. The mapping decomposes into permutation cycles; a cycle of length k needs k-1 arbitrary swaps because each swap can place one more item permanently.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.minimum_swaps_sort import minimum_swaps_sort

print(repr(minimum_swaps_sort([4, 3, 2, 1])))  # 2
```

## Boundary to remember

Duplicate values are rejected because they make the destination mapping ambiguous. This counts unrestricted pair swaps, not only adjacent swaps.

## Practice exercise

Count the minimum exchanges needed to sort a distinct set of numbered cards when any two positions may be swapped.
