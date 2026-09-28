# Guide a grid search with Manhattan distance

[Guide index](../README.md) · [Implementation](../../algorithm_lab/astar_grid.py)

## Reasoning

A* prioritizes the distance already traveled plus an optimistic estimate of
the remaining distance. On a grid with unit-cost horizontal and vertical moves,
Manhattan distance never overestimates the route: obstacles can only add steps.
Predecessors reconstruct a shortest route when the goal is reached. Heap work
takes O(V log V) time and the search state takes O(V) space.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.astar_grid import astar_grid
>>> grid = [[0, 0, 0], [1, 1, 0], [0, 0, 0]]
>>> astar_grid(grid, (0, 0), (2, 0))
[(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0)]
>>> astar_grid(grid, (0, 0), (1, 0)) is None
True
>>> astar_grid([[0]], (0, 0), (0, 0))
[(0, 0)]

```

## Boundary to remember

Coordinates are (row, column); 0 is open and 1 is blocked. A blocked endpoint
returns None, while an out-of-range coordinate or malformed grid raises
ValueError. Diagonal moves and variable movement costs are outside this API.
