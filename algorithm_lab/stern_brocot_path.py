"""Run-length paths to positive rationals in the Stern-Brocot tree.

Numerator and denominator are positive integers excluding bool. Return
(direction, count) runs from 1/1, where L decreases and R increases the
mediant. Equivalent unreduced fractions have the same path. Euclidean
division avoids expanding long runs: O(log(max(n,d))) steps and storage.

>>> stern_brocot_path(5, 2)
[('R', 2), ('L', 1)]
"""

from algorithm_lab._validation import integer


def stern_brocot_path(numerator, denominator):
    integer(numerator, "numerator", minimum=1)
    integer(denominator, "denominator", minimum=1)
    result = []
    while numerator != denominator:
        if numerator < denominator:
            count = (denominator - 1) // numerator
            result.append(("L", count))
            denominator -= count * numerator
        else:
            count = (numerator - 1) // denominator
            result.append(("R", count))
            numerator -= count * denominator
    return result
