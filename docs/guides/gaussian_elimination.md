# Solve linear equations and verify the substitution

[Guide index](../README.md) · [Implementation](../../algorithm_lab/gaussian_elimination.py)

## Reasoning

Row operations preserve a linear system’s solution set. Selecting a nonzero pivot and eliminating entries below it produces a triangular system, which can be solved backward. Exact Fractions let the final substitution recover the right-hand side without numerical tolerance.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.gaussian_elimination import gaussian_elimination
>>> matrix, rhs = [[0, 2], [3, 1]], [4, 5]
>>> solution = gaussian_elimination(matrix, rhs)
>>> solution
[Fraction(1, 1), Fraction(2, 1)]
>>> assert [sum(a*x for a, x in zip(row, solution)) for row in matrix] == rhs
>>> assert matrix == [[0, 2], [3, 1]]
>>> gaussian_elimination([], [])
[]

```

## Boundary to remember

This API solves square nonsingular rational systems. A singular system may have no solutions or many solutions, but neither case is returned as a single arbitrary solution.
