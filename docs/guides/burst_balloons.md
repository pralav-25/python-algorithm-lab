# Maximize coins earned by bursting balloons in any order.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/burst_balloons.py)

## Reasoning

Choose the last balloon to burst inside an interval. At that moment its neighbors are the interval boundaries, while the balloons on either side have already been removed. This turns an order-dependent process into two independent smaller intervals plus one final gain.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.burst_balloons import burst_balloons

print(repr(burst_balloons([3, 1, 5, 8])))  # 167
```

## Boundary to remember

Virtual balloons of value one sit at both ends. The input accepts nonnegative integers; an empty list earns zero, and tied optimal orders need not be reconstructed.

## Practice exercise

Find the best order for bursting a short row of balloons when each score depends on the neighbors still present.
