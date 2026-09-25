"""Factoradic selection of a lexicographic permutation.

n and rank are nonnegative integers excluding bool, with rank < n!.
Return the permutation of range(n) at that zero-based lexicographic rank.
O(n^2) time and O(n) space; n=0 admits only rank=0 and returns [].

>>> permutation_unrank(3, 4)
[2, 0, 1]
"""

from math import factorial

from algorithm_lab._validation import integer


def permutation_unrank(n, rank):
    integer(n, "n", minimum=0)
    integer(rank, "rank", minimum=0)
    total = factorial(n)
    if rank >= total:
        raise ValueError("permutation rank is out of range")
    remaining, result = list(range(n)), []
    for size in range(n, 0, -1):
        total //= size
        position, rank = divmod(rank, total)
        result.append(remaining.pop(position))
    return result
