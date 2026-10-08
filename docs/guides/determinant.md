# Track volume scaling through elimination

[Guide index](../README.md) · [Implementation](../../algorithm_lab/determinant.py)

## Reasoning

Elimination transforms a matrix into triangular form, whose determinant is the product of diagonal entries. Row swaps change the sign, while subtracting a multiple of one row from another preserves the determinant. Keeping those rules separate gives an exact determinant without cofactor expansion.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.determinant import determinant
>>> matrix = [[2, 0, 0], [0, 3, 0], [0, 0, 5]]
>>> determinant(matrix)
Fraction(30, 1)
>>> assert determinant([matrix[1], matrix[0], matrix[2]]) == -30
>>> determinant([[1, 2], [2, 4]])
Fraction(0, 1)
>>> determinant([])
Fraction(1, 1)

```

## Boundary to remember

A zero determinant signals singularity but does not by itself explain the system’s solution set. The empty matrix has determinant one by the multiplicative identity convention.

## Practice exercise

Subtract twice one row from another and verify that the exact determinant is unchanged. Check the original value with the two-by-two formula.

```pycon
>>> from algorithm_lab.determinant import determinant
>>> matrix = [[3, 2], [5, 7]]
>>> changed = [matrix[0][:], [matrix[1][j] - 2 * matrix[0][j] for j in range(2)]]
>>> assert determinant(matrix) == 3 * 7 - 2 * 5 == 11
>>> assert determinant(changed) == determinant(matrix)
>>> assert matrix == [[3, 2], [5, 7]]

```

Adding a multiple of a different row preserves the determinant. Scaling a row or swapping rows has a different effect, so those operations must not be treated as interchangeable elimination steps.
