"""Invert subset sums by Mobius inversion on bit masks.

Input is a nonempty integer array of power-of-two length, excluding bool.
Return the inverse of the subset zeta transform, leaving input unchanged.
O(n log n) integer operations and O(n) storage.

>>> subset_mobius_transform([1, 3, 4, 10])
[1, 2, 3, 4]
"""

from algorithm_lab._validation import integer


def subset_mobius_transform(values):
    result = list(values)
    n = len(result)
    if not n or n & (n - 1):
        raise ValueError("length must be a positive power of two")
    for value in result:
        integer(value)
    bit = 1
    while bit < n:
        for mask in range(n):
            if mask & bit:
                result[mask] -= result[mask ^ bit]
        bit <<= 1
    return result
