# Choose a cheapest route down a triangle

[Guide index](../README.md) · [Implementation](../../algorithm_lab/triangle_min_path.py)

## Reasoning

Starting from the bottom, the best suffix cost at a cell is its value plus the smaller of its two child suffix costs. Working upward makes both children available before their parent. Following the stored child choices then reconstructs a valid top-to-bottom route.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.triangle_min_path import triangle_min_path
>>> triangle = [[1], [5, 2], [4, 1, 6]]
>>> total, columns = triangle_min_path(triangle)
>>> total, columns
(4, [0, 1, 1])
>>> assert sum(triangle[row][column] for row, column in enumerate(columns)) == total
>>> assert all(b - a in (0, 1) for a, b in zip(columns, columns[1:]))
>>> triangle_min_path([])
(0, [])

```

## Boundary to remember

A step may stay in the same column or move to the next column, not jump to any cell in the next row. Negative entries are allowed, and equal child costs prefer the left child.
