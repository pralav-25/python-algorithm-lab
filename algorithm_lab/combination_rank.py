"""Lexicographic ranking of fixed-size combinations.

n is a nonnegative integer, and combination is a strictly increasing sequence
of integers from range(n), excluding bool. Return its zero-based index among
itertools.combinations(range(n), k). Empty combinations rank 0.
O(n) binomial evaluations and O(k) copied storage.

>>> combination_rank(5, [1, 3])
5
"""

from math import comb

from algorithm_lab._validation import integer


def combination_rank(n, combination):
    integer(n, "n", minimum=0)
    values = list(combination)
    previous, rank, k = -1, 0, len(values)
    for i, value in enumerate(values):
        integer(value, "element", minimum=0)
        if value <= previous or value >= n:
            raise ValueError("combination must be strictly increasing within range(n)")
        for skipped in range(previous + 1, value):
            rank += comb(n - skipped - 1, k - i - 1)
        previous = value
    return rank
