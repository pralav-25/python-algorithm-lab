"""Yield placements as tuples: entry row gives that row's queen column.

Columns are tried ascending, giving lexicographic order. Zero has one empty
placement. Bit-mask backtracking uses O(n) working slots and at most O(n*n!)
search/output operations. Big-int bit costs grow with n; recursive depth n
limits large inputs, and enumeration becomes impractical much earlier.

>>> list(n_queens(4))
[(1, 3, 0, 2), (2, 0, 3, 1)]
"""

from algorithm_lab._validation import integer


def n_queens(size):
    integer(size, "size", minimum=0)
    full = (1 << size) - 1
    path = []

    def place(columns, descending, ascending):
        if columns == full:
            yield tuple(path)
            return
        available = full & ~(columns | descending | ascending)
        while available:
            bit = available & -available
            available -= bit
            path.append(bit.bit_length() - 1)
            yield from place(
                columns | bit, ((descending | bit) << 1) & full, (ascending | bit) >> 1
            )
            path.pop()

    return place(0, 0, 0)
