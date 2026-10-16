# Return the minimum absolute difference between two distinct input positions.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/minimum_pair_difference.py)

## Reasoning

After sorting a copy, the closest pair must be adjacent: any value between a nonadjacent pair would be at least as close to one endpoint. A single pass over neighboring values therefore finds the minimum difference.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.minimum_pair_difference import minimum_pair_difference

print(repr(minimum_pair_difference([8, -3, 4, 10])))  # 2
```

## Boundary to remember

The pair must use two distinct input positions, so duplicate values correctly produce zero. Fewer than two values return None.

## Practice exercise

Find the smallest separation between two sensor readings, including repeated measurements.
