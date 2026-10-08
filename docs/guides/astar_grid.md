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

## Practice exercise

Route around a three-cell wall between two endpoints in the middle row. Certify the route length and every step without depending on which side A* chooses.

```pycon
>>> from algorithm_lab.astar_grid import astar_grid
>>> floor = [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]]
>>> route = astar_grid(floor, (1, 0), (1, 4))
>>> assert route[0] == (1, 0) and route[-1] == (1, 4)
>>> len(route) - 1
6
>>> assert all(floor[row][column] == 0 for row, column in route)
>>> assert all(abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1 for a, b in zip(route, route[1:]))

```

Four horizontal moves are unavoidable, and the wall forces one move away from the middle row and one back. Six moves are therefore both achievable and minimal.
