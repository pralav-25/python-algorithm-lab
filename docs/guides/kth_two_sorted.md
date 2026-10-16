# Select the zero-based kth value from the merge of two sorted sequences.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/kth_two_sorted.py)

## Reasoning

Choose a partition in each sorted input so the left sides contain exactly k+1 items. A valid partition has every left-side value no larger than every right-side value; binary search adjusts one partition until that condition holds.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.kth_two_sorted import kth_two_sorted

print(repr(kth_two_sorted([1, 3, 5], [2, 3, 8], 3)))  # 3
```

## Boundary to remember

k is zero-based and must identify an element in the combined inputs. Sortedness is assumed, and equal boundary values may be selected from either input.

## Practice exercise

Select a median from two already-sorted reports without first merging them into a new list.
