# Certify an exact floor root of any positive degree

[Guide index](../README.md) · [Implementation](../../algorithm_lab/integer_nth_root.py)

## Reasoning

For nonnegative inputs and positive degree, raising an integer candidate to that degree is monotonic. Binary search can therefore locate the last candidate whose power does not exceed the input. Exact exponentiation avoids deciding a boundary from a rounded floating-point root.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.integer_nth_root import integer_nth_root
>>> integer_nth_root(80, 3), integer_nth_root(81, 4)
(4, 3)
>>> value, degree = 10**120 + 123, 7
>>> root = integer_nth_root(value, degree)
>>> assert root**degree <= value < (root + 1)**degree
>>> integer_nth_root(123, 1)
123

```

## Boundary to remember

The result is a floor root. Negative inputs are outside this API even for odd degrees, and degree zero is not allowed.
