"""Build exact rational convergents with a two-term recurrence.

terms is an iterable of integers excluding bool; only the first may be
nonpositive. Return Fractions for all prefixes, or [] for empty input.
O(n) arithmetic operations and O(n) output space.

>>> continued_fraction_convergents([1, 2, 2])
[Fraction(1, 1), Fraction(3, 2), Fraction(7, 5)]
"""

from fractions import Fraction

from algorithm_lab._validation import integer


def continued_fraction_convergents(terms):
    p0, p1, q0, q1 = 0, 1, 1, 0
    result = []
    for i, term in enumerate(terms):
        integer(term, "term", minimum=1 if i else None)
        p0, p1 = p1, term * p1 + p0
        q0, q1 = q1, term * q1 + q0
        result.append(Fraction(p1, q1))
    return result
