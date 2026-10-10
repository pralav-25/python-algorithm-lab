"""Count ordered compositions of n into positive integer parts.

n is a nonnegative integer excluding bool; parts is None or a nonnegative
integer excluding bool. With parts=None count every length; otherwise count
exactly that length. The empty composition contributes 1 for n=0 and length 0.
Impossible lengths give 0; there are no ties. A binomial formula uses O(n)
arithmetic steps and O(1) integers, excluding big-integer costs.

>>> composition_count(5)
16
>>> composition_count(5, 2)
4
>>> composition_count(0, 0)
1
"""

from math import comb

from algorithm_lab._validation import integer


def composition_count(n, parts=None):
    integer(n, "n", minimum=0)
    if parts is None:
        return 1 if n == 0 else 1 << (n - 1)
    integer(parts, "parts", minimum=0)
    if n == 0:
        return int(parts == 0)
    if parts == 0 or parts > n:
        return 0
    return comb(n - 1, parts - 1)
