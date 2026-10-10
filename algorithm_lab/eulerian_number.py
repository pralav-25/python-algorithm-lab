"""Count permutations of n objects with exactly k descents.

n and k are nonnegative integers excluding bool. Return A(0,0)=1; impossible
descent counts return 0. There are no ties. Rolling dynamic programming uses
O(n*min(n,k+1)) arithmetic steps and O(min(n,k+1)) integer storage.

>>> eulerian_number(4, 1)
11
"""

from algorithm_lab._validation import integer


def eulerian_number(n, k):
    integer(n, "n", minimum=0)
    integer(k, "k", minimum=0)
    if n == 0:
        return int(k == 0)
    if k >= n:
        return 0
    row = [1] + [0] * k
    for size in range(1, n + 1):
        for descents in range(min(k, size - 1), 0, -1):
            row[descents] = (descents + 1) * row[descents] + (size - descents) * row[descents - 1]
    return row[k]
