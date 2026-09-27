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
