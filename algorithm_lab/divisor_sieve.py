"""Compute every positive divisor list through a bound.

Return lists indexed by integer 0..limit, each in ascending order; index 0
is empty. limit is a nonnegative integer excluding bool. O(n log n) time
and output storage, where n = limit.

>>> divisor_sieve(4)
[[], [1], [1, 2], [1, 3], [1, 2, 4]]
"""

from algorithm_lab._validation import integer


def divisor_sieve(limit):
    integer(limit, minimum=0)
    result = [[] for _ in range(limit + 1)]
    for divisor in range(1, limit + 1):
        for multiple in range(divisor, limit + 1, divisor):
            result[multiple].append(divisor)
    return result
