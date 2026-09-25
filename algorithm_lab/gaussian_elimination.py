"""Solve square rational linear systems by pivoted elimination.

Accept a square matrix and matching right-hand side of int/Fraction values,
excluding bool/float. Return exact Fractions without changing inputs. Empty
systems return []; singular systems raise ValueError. Pivots choose the first
nonzero remaining row. O(n^3) rational operations, O(n^2) space.

>>> gaussian_elimination([[2, 1], [1, -1]], [5, 1])
[Fraction(2, 1), Fraction(1, 1)]
"""

from fractions import Fraction


def gaussian_elimination(matrix, rhs):
    rows, rhs = [list(row) for row in matrix], list(rhs)
    n = len(rows)
    if len(rhs) != n or any(len(row) != n for row in rows):
        raise ValueError("a square matrix and matching rhs are required")
    if any(
        isinstance(v, bool) or not isinstance(v, (int, Fraction)) for row in rows for v in row
    ) or any(isinstance(v, bool) or not isinstance(v, (int, Fraction)) for v in rhs):
        raise ValueError("entries must be integers or Fractions")
    a = [[Fraction(v) for v in row] + [Fraction(b)] for row, b in zip(rows, rhs, strict=True)]
    for column in range(n):
        pivot = next((i for i in range(column, n) if a[i][column]), None)
        if pivot is None:
            raise ValueError("matrix is singular")
        a[column], a[pivot] = a[pivot], a[column]
        scale = a[column][column]
        a[column] = [value / scale for value in a[column]]
        for i in range(column + 1, n):
            factor = a[i][column]
            a[i] = [v - factor * w for v, w in zip(a[i], a[column], strict=True)]
    result = [Fraction(0)] * n
    for i in range(n - 1, -1, -1):
        result[i] = a[i][-1] - sum(a[i][j] * result[j] for j in range(i + 1, n))
    return result
