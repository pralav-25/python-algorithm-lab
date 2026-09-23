"""Return (scalar multiplication count, parenthesization) for a matrix chain.

Dimensions [d0, d1, ..., dn] describe n matrices of size di × d(i+1). Require at
least one matrix and positive integer dimensions. Ties choose the first split.
Time O(n³), space O(n²), with O(n) recursive reconstruction depth.

>>> matrix_chain([10, 30, 5, 60])
(4500, '((A1 @ A2) @ A3)')
"""


def matrix_chain(dimensions) -> tuple[int, str]:
    dimensions = list(dimensions)
    if len(dimensions) < 2 or any(
        isinstance(d, bool) or not isinstance(d, int) or d <= 0 for d in dimensions
    ):
        raise ValueError("provide at least two positive integer dimensions")
    size = len(dimensions) - 1
    costs = [[0] * size for _ in range(size)]
    splits = [[0] * size for _ in range(size)]
    for length in range(2, size + 1):
        for first in range(size - length + 1):
            last = first + length - 1
            best = None
            for middle in range(first, last):
                candidate = (
                    costs[first][middle]
                    + costs[middle + 1][last]
                    + dimensions[first] * dimensions[middle + 1] * dimensions[last + 1]
                )
                if best is None or candidate < best:
                    best, splits[first][last] = candidate, middle
            costs[first][last] = best

    def describe(first, last):
        if first == last:
            return f"A{first + 1}"
        middle = splits[first][last]
        return f"({describe(first, middle)} @ {describe(middle + 1, last)})"

    return costs[0][-1], describe(0, size - 1)
