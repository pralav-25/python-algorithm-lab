"""Tie-adjusted Kendall rank correlation tau-b.

Inputs are equal-length finite int/float observations, excluding bool, with
at least two pairs. Return tau-b, accounting separately for ties on each
axis. A constant axis raises ValueError because the denominator is zero.
O(n^2) comparisons and O(n) copied storage. Ordering uses validated floats.

>>> kendall_tau([1, 2, 3], [3, 2, 1])
-1.0
"""

from math import sqrt

from algorithm_lab._numeric import finite


def kendall_tau(left, right):
    left, right = [finite(x) for x in left], [finite(x) for x in right]
    if len(left) != len(right) or len(left) < 2:
        raise ValueError("at least two paired observations are required")
    concordance, untied_left, untied_right = 0, 0, 0
    for i in range(len(left)):
        for j in range(i):
            a = (left[i] > left[j]) - (left[i] < left[j])
            b = (right[i] > right[j]) - (right[i] < right[j])
            concordance += a * b
            untied_left += a != 0
            untied_right += b != 0
    if not untied_left or not untied_right:
        raise ValueError("correlation is undefined for a constant axis")
    return concordance / sqrt(untied_left * untied_right)
