"""Enumerate reduced fractions in [0,1] with denominator at most order.

order is a positive integer excluding bool. Return a new list of Fraction
objects, increasing with no duplicates, including both 0/1 and 1/1. Equal
fractions occur once. The neighbor recurrence uses O(order**2) arithmetic steps
and output storage, excluding arbitrary-precision and Fraction reduction costs.

>>> farey_sequence(3)
[Fraction(0, 1), Fraction(1, 3), Fraction(1, 2), Fraction(2, 3), Fraction(1, 1)]
"""

from fractions import Fraction

from algorithm_lab._validation import integer


def farey_sequence(order):
    integer(order, "order", minimum=1)
    a, b, c, d = 0, 1, 1, order
    result = [Fraction(a, b)]
    while c <= order:
        result.append(Fraction(c, d))
        quotient = (order + b) // d
        a, b, c, d = c, d, quotient * c - a, quotient * d - b
    return result
