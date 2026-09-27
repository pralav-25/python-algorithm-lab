# Locate the largest all-one square

[Guide index](../README.md) · [Implementation](../../algorithm_lab/maximal_square.py)

## Reasoning

For a cell containing one, a square ending there can grow only as far as the smallest square above, left, and diagonally above-left. Adding one to that minimum gives its side length. Remembering the largest side and corresponding origin reconstructs a square rather than only reporting its area.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.maximal_square import maximal_square
>>> matrix = [[0, 1, 1], [0, 1, 1], [1, 1, 1]]
>>> side, top, left = maximal_square(matrix)
>>> side, top, left
(2, 0, 1)
>>> assert all(matrix[row][col] == 1 for row in range(top, top+side) for col in range(left, left+side))
>>> maximal_square([[0, 0]])
(0, None, None)

```

## Boundary to remember

The result reports side length, not area. A matrix with no ones returns coordinates of None, and equal-size squares prefer the smallest row-column origin.
