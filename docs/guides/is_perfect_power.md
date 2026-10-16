# Decide whether n=a**b for integers a>=2 and b>=2.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/is_perfect_power.py)

## Reasoning

For each possible exponent, binary-search for an integer root and compare powers exactly. This avoids floating-point root rounding, which can misclassify large integers near a perfect-power boundary.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.is_perfect_power import is_perfect_power

print(repr(is_perfect_power(81)))  # True
```

## Boundary to remember

Only integers greater than one are accepted, and both base and exponent must be at least two. The function answers existence without choosing one of several representations.

## Practice exercise

Determine whether a large integer is a square, cube, or higher integer power without using floating-point roots.
