# Divide a polynomial while retaining an exact remainder

[Guide index](../README.md) · [Implementation](../../algorithm_lab/polynomial_divmod.py)

## Reasoning

Cancel the highest remaining degree by subtracting a suitable shifted multiple of the divisor. Each cancellation lowers the degree until the remainder is smaller than the divisor. Rational coefficients are necessary because an integer dividend divided by an integer polynomial can have fractional quotient coefficients.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.polynomial_divmod import polynomial_divmod
>>> dividend, divisor = [3, 3, 1], [1, 1]
>>> quotient, remainder = polynomial_divmod(dividend, divisor)
>>> quotient, remainder
([Fraction(2, 1), Fraction(1, 1)], [Fraction(1, 1)])
>>> evaluate = lambda coefficients, x: sum(c * x**i for i, c in enumerate(coefficients))
>>> assert all(
...     evaluate(dividend, x) == evaluate(quotient, x) * evaluate(divisor, x) + evaluate(remainder, x)
...     for x in [-2, 0, 3]
... )

```

## Boundary to remember

Inputs use increasing-degree coefficients and reject floats. The identity dividend = quotient*divisor + remainder is the main correctness certificate; a zero remainder is represented by an empty list.
