"""Find the minimum top-left to bottom-right path cost with right/down steps.

Grid is an iterable of equally long row iterables containing integers; bool is
rejected and negative costs are allowed. A nonempty grid must have at least one
column. Both endpoint costs count. Return the minimum integer cost, zero for an
empty grid; tied paths need no selection. O(r*c) time and space excluding
integer arithmetic. Rows are copied, never mutated.

>>> minimum_cost_path_grid([[1, 3, 1], [1, 5, 1], [4, 2, 1]])
7
"""

from algorithm_lab._validation import integer


def minimum_cost_path_grid(grid) -> int:
    rows = [list(row) for row in grid]
    if not rows:
        return 0
    columns = len(rows[0])
    if not columns or any(len(row) != columns for row in rows):
        raise ValueError("nonempty grid must be rectangular with nonempty rows")
    for row in rows:
        for value in row:
            integer(value, "grid cost")
    costs = [0] * columns
    for row_index, row in enumerate(rows):
        for column, value in enumerate(row):
            if not row_index and not column:
                costs[column] = value
            elif not row_index:
                costs[column] = costs[column - 1] + value
            elif not column:
                costs[column] += value
            else:
                costs[column] = min(costs[column], costs[column - 1]) + value
    return costs[-1]
