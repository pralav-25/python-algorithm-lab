"""Minimum sum down an integer triangle with path reconstruction.

Row i must contain i+1 integers, excluding bool. Each step goes to the same
or next column in the following row. Return (sum, column_indices), preferring
the left child on ties. Empty input returns (0, []). O(n^2) time and space
for n rows; inputs remain unchanged.

>>> triangle_min_path([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
(11, [0, 0, 1, 1])
"""

from algorithm_lab._validation import integer


def triangle_min_path(triangle):
    rows = [list(row) for row in triangle]
    for i, row in enumerate(rows):
        if len(row) != i + 1:
            raise ValueError("row i must have i+1 entries")
        for value in row:
            integer(value, "entry")
    if not rows:
        return 0, []
    scores = rows[-1][:]
    choices = [None] * (len(rows) - 1)
    for i in range(len(rows) - 2, -1, -1):
        choices[i] = [int(scores[j + 1] < scores[j]) for j in range(i + 1)]
        scores = [rows[i][j] + scores[j + choices[i][j]] for j in range(i + 1)]
    path, column = [0], 0
    for row in choices:
        column += row[column]
        path.append(column)
    return scores[0], path
