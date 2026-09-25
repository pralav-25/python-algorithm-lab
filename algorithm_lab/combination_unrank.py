"""Select a lexicographic combination without enumerating predecessors.

Integers satisfy 0 <= k <= n and 0 <= rank < C(n,k); bool is rejected.
Return a list matching itertools.combinations(range(n), k)[rank]. O(n)
binomial evaluations and O(k) output space. The empty combination has rank 0.

>>> combination_unrank(5, 2, 5)
[1, 3]
"""

from math import comb

from algorithm_lab._validation import integer


def combination_unrank(n, k, rank):
    integer(n, "n", minimum=0)
    integer(k, "k", minimum=0)
    integer(rank, "rank", minimum=0)
    if k > n or rank >= comb(n, k):
        raise ValueError("combination rank is out of range")
    result, candidate = [], 0
    while len(result) < k:
        count = comb(n - candidate - 1, k - len(result) - 1)
        if rank < count:
            result.append(candidate)
        else:
            rank -= count
        candidate += 1
    return result
