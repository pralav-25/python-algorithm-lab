"""Count partitions into a specified number of nonempty blocks.

n and k are nonnegative integers excluding bool. S(0,0)=1, and S(n,k)=0
when k>n. Rolling dynamic programming uses O(n*min(n,k)) arithmetic steps
and O(min(n,k)) space; all counts are exact integers.

>>> stirling_second(5, 2)
15
"""

from algorithm_lab._validation import integer


def stirling_second(n, k):
    integer(n, "n", minimum=0)
    integer(k, "k", minimum=0)
    if k > n:
        return 0
    row = [1] + [0] * k
    for i in range(1, n + 1):
        for j in range(min(i, k), 0, -1):
            row[j] = j * row[j] + row[j - 1]
        row[0] = 0
    return row[k]
