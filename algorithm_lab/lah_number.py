"""Count partitions of n labeled objects into k unordered ordered lists.

n and k are nonnegative integers excluding bool. Return an unsigned Lah number;
L(0,0)=1, and impossible block counts return 0. There are no ties. The closed
formula uses O(n) arithmetic steps and O(1) integers, excluding big-integer costs.

>>> lah_number(4, 2)
36
"""

from math import comb, factorial

from algorithm_lab._validation import integer


def lah_number(n, k):
    integer(n, "n", minimum=0)
    integer(k, "k", minimum=0)
    if n == 0:
        return int(k == 0)
    if k == 0 or k > n:
        return 0
    return comb(n - 1, k - 1) * factorial(n) // factorial(k)
