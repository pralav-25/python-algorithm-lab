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
>>> assert root**degree <= value < (root + 1) ** degree
>>> integer_nth_root(123, 1)
123

```

## Boundary to remember

The result is a floor root. Negative inputs are outside this API even for odd degrees, and degree zero is not allowed.

## Practice exercise

Classify candidate values as perfect fourth powers by checking the returned floor root. Include both neighbors of 81 so rounding cannot hide a boundary.

```pycon
>>> from algorithm_lab.integer_nth_root import integer_nth_root
>>> values = [16, 80, 81, 82, 256]
>>> roots = [integer_nth_root(value, 4) for value in values]
>>> roots
[2, 2, 3, 3, 4]
>>> [root**4 == value for value, root in zip(values, roots)]
[True, False, True, False, True]
>>> assert all(root**4 <= value < (root + 1) ** 4 for value, root in zip(values, roots))

```

Values 81 and 82 have the same floor root, so the root alone cannot certify a perfect power. Raising it back to the requested degree gives the exact certificate. No floating-point tolerance is appropriate for this integer decision.
