"""Return row n of Pascal's triangle, starting row zero at [1].

O(n) arithmetic operations, O(n) output slots; arbitrary-size integers remain
exact. The input must be a nonnegative integer, excluding bool.

>>> pascal_row(4)
[1, 4, 6, 4, 1]
"""

from algorithm_lab._validation import integer


def pascal_row(n):
    integer(n, "n", minimum=0)
    row = [1]
    for k in range(1, n + 1):
        row.append(row[-1] * (n - k + 1) // k)
    return row
