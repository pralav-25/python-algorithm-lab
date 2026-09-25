"""Exact dense polynomial convolution.

Inputs contain integers in increasing degree order, excluding bool.
Return canonical coefficients with trailing zeros removed; zero is [].
Inputs are copied. O(n*m) arithmetic steps and O(n+m) space.

>>> polynomial_multiply([1, 2], [-1, 3])
[-1, 1, 6]
"""

from algorithm_lab._validation import integer


def polynomial_multiply(left, right):
    left, right = list(left), list(right)
    for value in left + right:
        integer(value, "coefficient")
    if not left or not right:
        return []
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    while result and result[-1] == 0:
        result.pop()
    return result
