"""All-pairs shortest paths from a square adjacency matrix in O(n³) time.

Missing edges use positive infinity; finite int/float weights may be negative.
Boolean weights, NaN, and negative infinity are invalid. Diagonal distances start
at min(0, supplied value). Any negative cycle raises ValueError. Space O(n²).

>>> floyd_warshall([[0, 3, float('inf')], [float('inf'), 0, -1], [4, float('inf'), 0]])
[[0, 3, 2], [3, 0, -1], [4, 7, 0]]
"""

import math

from algorithm_lab._weighted_graph import path_cost


def floyd_warshall(matrix):
    size = len(matrix)
    if any(len(row) != size for row in matrix):
        raise ValueError("matrix must be square")
    distances = [list(row) for row in matrix]
    for i, row in enumerate(distances):
        for value in row:
            if (
                isinstance(value, bool)
                or not isinstance(value, (int, float))
                or (isinstance(value, float) and (math.isnan(value) or value == -math.inf))
            ):
                raise ValueError("weights must be finite numbers or positive infinity")
        row[i] = min(0, row[i])
    for middle in range(size):
        for start in range(size):
            if distances[start][middle] == math.inf:
                continue
            for end in range(size):
                if distances[middle][end] != math.inf:
                    candidate = path_cost(distances[start][middle], distances[middle][end])
                    distances[start][end] = min(distances[start][end], candidate)
    if any(distances[i][i] < 0 for i in range(size)):
        raise ValueError("graph contains a negative cycle")
    return distances
