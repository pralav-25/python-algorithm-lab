"""Compute n*(n-1)*...*(n-k+1), including negative integer n.

n is any integer and k is a nonnegative integer, both excluding bool. Return
an exact integer; k=0 gives the empty product 1. There are no ties. O(k)
arithmetic steps and O(1) integers of storage, excluding big-integer costs.

>>> falling_factorial(5, 3)
60
>>> falling_factorial(-2, 3)
-24
"""

from algorithm_lab._validation import integer


def falling_factorial(n, k):
    integer(n, "n")
    integer(k, "k", minimum=0)
    result = 1
    for offset in range(k):
        result *= n - offset
    return result
