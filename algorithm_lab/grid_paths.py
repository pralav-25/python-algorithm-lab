"""Count paths from top-left to bottom-right on a rectangular binary grid.

Only right/down moves are allowed. 0/False is open; 1/True is blocked. Empty
rectangles return zero, and malformed grids raise ValueError. Python integers
retain exact counts. Time O(rows * columns), extra space O(columns).

>>> grid_paths([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
2
"""


def grid_paths(grid) -> int:
    if not grid:
        return 0
    columns = len(grid[0])
    if any(len(row) != columns for row in grid):
        raise ValueError("grid must be rectangular")
    if any(type(cell) not in (int, bool) or cell not in (0, 1) for row in grid for cell in row):
        raise ValueError("grid cells must be 0 or 1")
    if not columns:
        return 0
    counts = [0] * columns
    counts[0] = 1
    for row in grid:
        for column, blocked in enumerate(row):
            if blocked:
                counts[column] = 0
            elif column:
                counts[column] += counts[column - 1]
    return counts[-1]
