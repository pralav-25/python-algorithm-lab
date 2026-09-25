"""Canonical finite continued fractions for rational inputs.

Accept integer numerator and nonzero integer denominator, excluding bool.
Return [a0, a1, ...], with a0 the floor and later terms positive. The final
term is > 1 unless the result is integral. O(log(max(|n|, |d|)+1)) Euclidean
steps and O(number of terms) output space.

>>> continued_fraction(43, 19)
[2, 3, 1, 4]
"""

from algorithm_lab._validation import integer


def continued_fraction(numerator, denominator):
    integer(numerator, "numerator")
    integer(denominator, "denominator")
    if denominator == 0:
        raise ValueError("denominator must be nonzero")
    if denominator < 0:
        numerator, denominator = -numerator, -denominator
    result = []
    while denominator:
        term, remainder = divmod(numerator, denominator)
        result.append(term)
        numerator, denominator = denominator, remainder
    return result
