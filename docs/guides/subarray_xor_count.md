# Count nonempty contiguous subarrays whose XOR equals target.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/subarray_xor_count.py)

## Reasoning

If the XOR before a range is p and the target is t, the XOR after it must be p XOR t because XOR is its own inverse. Store frequencies of earlier prefix XORs to count all matching ranges ending at each position.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.subarray_xor_count import subarray_xor_count

print(repr(subarray_xor_count([4, 2, 2, 6, 4], 6)))  # 4
```

## Boundary to remember

Only nonnegative integers and a nonnegative target are accepted. The empty range is excluded, while overlapping ranges and repeated values count independently.

## Practice exercise

Count all contiguous sensor windows whose bitwise XOR equals a chosen alert mask.
