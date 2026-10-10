"""Count permutations of n objects with exactly k fixed points.

n and k are nonnegative integers excluding bool. Return R(0,0)=1; k>n returns 0.
There are no ties. A derangement recurrence and binomial coefficient use O(n)
arithmetic steps and O(1) integers, excluding arbitrary-precision costs.

>>> rencontres_number(4, 2)
6
"""

from math import comb

from algorithm_lab._validation import integer


def rencontres_number(n, k):
    integer(n, "n", minimum=0)
    integer(k, "k", minimum=0)
    if k > n:
        return 0
    remaining = n - k
    previous, current = 1, 0
    if remaining == 0:
        return 1
    for size in range(2, remaining + 1):
        previous, current = current, (size - 1) * (current + previous)
    return comb(n, k) * current
