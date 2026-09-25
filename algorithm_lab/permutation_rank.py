"""Lehmer-code ranking of permutations of range(n).

Input must contain each integer in range(n) once, excluding bool. Return the
zero-based lexicographic rank, with the empty permutation ranked 0. O(n^2)
time and O(n) storage using a sorted list of remaining values.

>>> permutation_rank([2, 0, 1])
4
"""

from algorithm_lab._validation import integer


def permutation_rank(permutation):
    values = list(permutation)
    for value in values:
        integer(value)
    n = len(values)
    if set(values) != set(range(n)):
        raise ValueError("input must be a permutation of range(n)")
    remaining, rank = list(range(n)), 0
    for value in values:
        position = remaining.index(value)
        rank = rank * len(remaining) + position
        remaining.pop(position)
    return rank
