"""Largest all-one square with deterministic coordinates.

Accept a rectangular matrix of integer 0/1 entries, excluding bool. Return
(side_length, top_row, left_column); no square returns (0, None, None).
Equal-size squares prefer the smallest (top_row, left_column). O(rows*cols)
time and copied input space, with O(cols) dynamic-programming workspace.

>>> maximal_square([[1, 1, 0], [1, 1, 1]])
(2, 0, 0)
"""


def maximal_square(matrix):
    rows = [list(row) for row in matrix]
    width = len(rows[0]) if rows else 0
    if any(len(row) != width for row in rows):
        raise ValueError("matrix must be rectangular")
    if any(type(value) is not int or value not in (0, 1) for row in rows for value in row):
        raise ValueError("entries must be integer zero or one")
    previous, best = [0] * (width + 1), (0, None, None)
    for i, row in enumerate(rows):
        current = [0] * (width + 1)
        for j, value in enumerate(row):
            if value:
                size = 1 + min(previous[j], previous[j + 1], current[j])
                current[j + 1] = size
                candidate = (size, i - size + 1, j - size + 1)
                if size > best[0] or (size == best[0] and candidate[1:] < best[1:]):
                    best = candidate
        previous = current
    return best
