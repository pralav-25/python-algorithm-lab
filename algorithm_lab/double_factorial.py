"""Multiply n, n-2, n-4, and so on down to 1 or 2.

n is an integer >=-1 excluding bool. Return an exact integer, using the
conventions (-1)!!=0!!=1. There are no ties. O(max(n,0)) arithmetic steps and
O(1) integers of storage; arbitrary-precision integer costs are additional.

>>> double_factorial(7)
105
"""

from algorithm_lab._validation import integer


def double_factorial(n):
    integer(n, "n", minimum=-1)
    result = 1
    for value in range(n, 0, -2):
        result *= value
    return result
