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
>>> assert all(
...     matrix[row][col] == 1 for row in range(top, top + side) for col in range(left, left + side)
... )
>>> maximal_square([[0, 0]])
(0, None, None)

```

## Boundary to remember

The result reports side length, not area. A matrix with no ones returns coordinates of None, and equal-size squares prefer the smallest row-column origin.

## Practice exercise

Locate a square when two separate blocks have the same maximum side
length, and turn the returned side into an area.

```pycon
>>> from algorithm_lab.maximal_square import maximal_square
>>> tiles = [[1, 1, 0, 1, 1], [1, 1, 0, 1, 1]]
>>> side, row, column = maximal_square(tiles)
>>> side, row, column, side * side
(2, 0, 0, 4)
>>> assert [line[column : column + side] for line in tiles[row : row + side]] == [[1, 1], [1, 1]]
>>> assert maximal_square([[], []]) == (0, None, None)

```

The zero column prevents the two blocks from joining. Tied squares use
the smallest origin, and the area is the square of the reported side;
confusing those two measurements produces the wrong result.
