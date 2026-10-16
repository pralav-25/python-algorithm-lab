# Return the largest adjacent gap in the sorted order of signed integers.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/maximum_gap.py)

## Reasoning

The largest adjacent gap after sorting must occur between buckets, not inside a bucket chosen narrower than the average gap. Track each bucket's minimum and maximum, then compare each nonempty bucket minimum with the previous nonempty bucket maximum.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.maximum_gap import maximum_gap

print(repr(maximum_gap([3, 6, 9, 1])))  # 3
```

## Boundary to remember

Fewer than two values and all-equal values return zero. The input is copied; the linear-time bound assumes ordinary unit-cost integer arithmetic.

## Practice exercise

Find the widest empty interval between sorted integer measurements without sorting every value explicitly.
