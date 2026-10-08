# Count right-and-down routes around obstacles

[Guide index](../README.md) · [Implementation](../../algorithm_lab/grid_paths.py)

## Reasoning

The number of ways to reach an open cell is the sum of ways to reach its upper and left neighbors. A blocked cell contributes zero and cuts off paths that would pass through it. One row of counts is enough because each new row only needs the previous row and its own previous cell.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.grid_paths import grid_paths
>>> grid_paths([[0, 0, 0], [0, 0, 0]])
3
>>> grid_paths([[0, 1, 0], [0, 0, 0]])
1
>>> grid_paths([[1, 0], [0, 0]])
0
>>> grid_paths([[0]])
1

```

## Boundary to remember

Movement is restricted to right and down. This is not a general maze search and cannot represent detours that move upward or left. A blocked start or destination gives zero paths.

## Practice exercise

Count routes across a four-row, five-column board, then block cell (1, 2). Derive the lost routes by multiplying the number of prefixes and suffixes through that cell.

```pycon
>>> from math import comb
>>> from algorithm_lab.grid_paths import grid_paths
>>> board = [[0] * 5 for _ in range(4)]
>>> grid_paths(board)
35
>>> assert grid_paths(board) == comb(7, 3)
>>> board[1][2] = 1
>>> grid_paths(board)
17
>>> assert grid_paths(board) == comb(7, 3) - comb(3, 1) * comb(4, 2)

```

An unobstructed route chooses the positions of its three down moves among seven moves. A route through the blocked cell has three possible prefixes and six possible suffixes. Each lost route has exactly one such decomposition, so subtracting 18 gives an independent check of the dynamic program.
