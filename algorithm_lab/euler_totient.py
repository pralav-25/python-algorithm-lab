"""Count coprime residues by prime factorization.

n is a positive integer, excluding bool. phi(1) is 1. Trial division takes
O(sqrt(n)) arithmetic steps and O(1) integer storage.

>>> euler_totient(36)
12
"""

from algorithm_lab._validation import integer


def euler_totient(n):
    integer(n, minimum=1)
    result, remaining, factor = n, n, 2
    while factor * factor <= remaining:
        if remaining % factor == 0:
            result -= result // factor
            while remaining % factor == 0:
                remaining //= factor
        factor += 1
    if remaining > 1:
        result -= result // remaining
    return result
