"""Integer matrix powers by repeated squaring.

The matrix must be square with integer entries; exponent is a nonnegative
integer. Booleans are rejected. Return a new matrix; exponent 0 returns the
identity (including [] for the empty matrix). O(n^3 log(exponent+1)) integer
operations and O(n^2) storage.

>>> matrix_power([[1, 1], [1, 0]], 5)
[[8, 5], [5, 3]]
"""

from algorithm_lab._validation import integer


def matrix_power(matrix, exponent):
    integer(exponent, "exponent", minimum=0)
    a = [list(row) for row in matrix]
    n = len(a)
    if any(len(row) != n for row in a):
        raise ValueError("matrix must be square")
    for row in a:
        for value in row:
            integer(value, "entry")

    def multiply(left, right):
        return [
            [sum(left[i][k] * right[k][j] for k in range(n)) for j in range(n)] for i in range(n)
        ]

    result = [[int(i == j) for j in range(n)] for i in range(n)]
    while exponent:
        if exponent & 1:
            result = multiply(result, a)
        exponent //= 2
        if exponent:
            a = multiply(a, a)
    return result
