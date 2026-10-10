"""Sum all positive divisors of a positive integer.

n is a positive integer excluding bool. Return an exact integer, with sum 1 for
n=1. There are no ties. Trial factorization uses O(sqrt(n)) arithmetic steps
and O(1) integer storage, excluding arbitrary-precision costs.

>>> divisor_sum(28)
56
"""

from algorithm_lab._validation import integer


def divisor_sum(n):
    integer(n, "n", minimum=1)
    remaining, factor, result = n, 2, 1
    while factor * factor <= remaining:
        power, subtotal = 1, 1
        while remaining % factor == 0:
            remaining //= factor
            power *= factor
            subtotal += power
        result *= subtotal
        factor += 1
    if remaining > 1:
        result *= remaining + 1
    return result
