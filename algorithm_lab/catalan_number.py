"""Return the nth Catalan number for a nonnegative integer n.

O(n) arithmetic operations and O(1) integer slots; big-integer cost and storage
grow with n. Counts balanced parentheses, full binary tree shapes, and other
Catalan families. Booleans and non-integers are rejected.

>>> [catalan_number(n) for n in range(6)]
[1, 1, 2, 5, 14, 42]
"""

from algorithm_lab._validation import integer


def catalan_number(n):
    integer(n, "n", minimum=0)
    result = 1
    for k in range(n):
        result = result * 2 * (2 * k + 1) // (k + 2)
    return result
