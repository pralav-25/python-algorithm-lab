# Return the largest h with at least h citation counts greater than or equal to h.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/h_index.py)

## Reasoning

A paper with at least n citations can never affect an h-index above n. Count citations into n+1 buckets, placing every larger value in the last bucket, then accumulate from high counts downward until enough papers support that candidate.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.h_index import h_index

print(repr(h_index([3, 0, 6, 1, 5])))  # 3
```

## Boundary to remember

Duplicate citation counts belong to separate papers. Negative values and booleans are rejected, while an empty list has h-index zero.

## Practice exercise

Summarize a reviewer's citation counts without sorting every paper individually.
