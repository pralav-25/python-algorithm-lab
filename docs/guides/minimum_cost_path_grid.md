# Find the minimum top-left to bottom-right path cost with right/down steps.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/minimum_cost_path_grid.py)

## Reasoning

Each cell can only be reached from above or from the left. Store the cheapest cost to reach each cell, including that cell's cost, and the bottom-right state gives the best monotone path.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.minimum_cost_path_grid import minimum_cost_path_grid

print(repr(minimum_cost_path_grid([[1, 3, 1], [1, 5, 1], [4, 2, 1]])))  # 7
```

## Boundary to remember

Both endpoint cells count toward the total, and negative integer costs are supported because movement never revisits a cell. Empty input returns zero; nonempty rows must have equal positive width.

## Practice exercise

Route through a cost grid with only right and down moves, counting both the starting and ending cells.
