"""Horner evaluation of integer polynomials.

Coefficients are integers in increasing degree order; x is an integer.
Booleans are rejected. An empty polynomial evaluates to 0. O(n) arithmetic
steps and O(n) copied storage; input is not modified.

>>> polynomial_evaluate([1, -2, 3], 4)
41
"""

from algorithm_lab._validation import integer


def polynomial_evaluate(coefficients, x):
    integer(x, "x")
    values = list(coefficients)
    for coefficient in values:
        integer(coefficient, "coefficient")
    result = 0
    for coefficient in reversed(values):
        result = result * x + coefficient
    return result
