"""Count positive divisors of a positive integer.

n is a positive integer excluding bool. Return an exact integer, with 1 having
one divisor. There are no ties. Trial factorization uses O(sqrt(n)) arithmetic
steps and O(1) integer storage, excluding arbitrary-precision costs.

>>> divisor_count(36)
9
"""

from algorithm_lab._validation import integer


def divisor_count(n):
    integer(n, "n", minimum=1)
    remaining, factor, result = n, 2, 1
    while factor * factor <= remaining:
        exponent = 0
        while remaining % factor == 0:
            remaining //= factor
            exponent += 1
        result *= exponent + 1
        factor += 1
    if remaining > 1:
        result *= 2
    return result
