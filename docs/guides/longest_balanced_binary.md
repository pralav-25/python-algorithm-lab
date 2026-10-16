# Return half-open indices of the longest subarray with equal zeros and ones.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/longest_balanced_binary.py)

## Reasoning

Treat zero as -1 and one as +1. Equal prefix sums mark a balanced interval between their indices; retaining the earliest index for each sum makes that interval as long as possible.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.longest_balanced_binary import longest_balanced_binary

print(repr(longest_balanced_binary([0, 1, 0])))  # (0, 2)
```

## Boundary to remember

Only integer zero and one are accepted, with booleans excluded. Equal-length answers choose the smallest start, and no nonempty balanced interval returns (0, 0).

## Practice exercise

Find the longest range in a binary event stream where two event types occur equally often.
