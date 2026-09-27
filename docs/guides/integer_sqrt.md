# Bound a square root without floating-point rounding

[Guide index](../README.md) · [Implementation](../../algorithm_lab/integer_sqrt.py)

## Reasoning

Integer Newton iteration starts from a safe upper estimate and repeatedly improves it using division. The desired result is characterized by two exact inequalities: r squared is at most the input, and (r+1) squared is larger. Those inequalities remain meaningful even far beyond floating-point precision.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.integer_sqrt import integer_sqrt
>>> root = 10**50 + 7
>>> integer_sqrt(root * root - 1) == root - 1
True
>>> value = 10**101 + 123
>>> result = integer_sqrt(value)
>>> assert result * result <= value < (result + 1) * (result + 1)
>>> integer_sqrt(0)
0

```

## Boundary to remember

The function returns a floor, not the nearest integer and not a decimal approximation. A value just below a large square must return one less than that square’s root.
