"""Compute exact determinants by elimination.

Input is a square matrix of int/Fraction values, excluding bool/float.
Return a Fraction; the empty determinant is 1. Singular matrices return 0.
First nonzero row pivoting is deterministic. O(n^3) rational operations and
O(n^2) copied storage; the input is unchanged.

>>> determinant([[1, 2], [3, 4]])
Fraction(-2, 1)
"""

from fractions import Fraction


def determinant(matrix):
    a = [list(row) for row in matrix]
    n = len(a)
    if any(len(row) != n for row in a):
        raise ValueError("matrix must be square")
    if any(isinstance(v, bool) or not isinstance(v, (int, Fraction)) for row in a for v in row):
        raise ValueError("entries must be integers or Fractions")
    a = [[Fraction(v) for v in row] for row in a]
    result = Fraction(1)
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            result = -result
        result *= a[j][j]
        for i in range(j + 1, n):
            factor = a[i][j] / a[j][j]
            for k in range(j + 1, n):
                a[i][k] -= factor * a[j][k]
    return result
