# Return unique sorted 3-tuples summing to target, in lexicographic order.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/three_sum.py)

## Reasoning

Sort a copy, fix one value, and use two pointers to search the remaining suffix. The sum's direction tells which pointer can move without losing a possible solution; skipping duplicate values yields unique tuples.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.three_sum import three_sum

print(repr(three_sum([-1, 0, 1, 2, -1, -4])))  # [(-1, -1, 2), (-1, 0, 1)]
```

## Boundary to remember

Every tuple uses three distinct input positions. Values may repeat, but each returned value tuple is unique, internally sorted, and ordered lexicographically.

## Practice exercise

Find every unique trio of expenses that sums to a budget while allowing repeated expense amounts.
