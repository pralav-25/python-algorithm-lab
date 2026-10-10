"""Count Dyck paths of semilength n with exactly k peaks.

n and k are nonnegative integers excluding bool. The empty path gives N(0,0)=1;
impossible peak counts give 0. There are no ties. Two binomial coefficients use
O(n) arithmetic steps and O(1) integers, excluding arbitrary-precision costs.

>>> narayana_number(4, 2)
6
"""

from math import comb

from algorithm_lab._validation import integer


def narayana_number(n, k):
    integer(n, "n", minimum=0)
    integer(k, "k", minimum=0)
    if n == 0:
        return int(k == 0)
    if k == 0 or k > n:
        return 0
    return comb(n, k) * comb(n, k - 1) // n
