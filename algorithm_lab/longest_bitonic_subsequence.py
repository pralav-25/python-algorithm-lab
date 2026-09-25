"""Reconstruct a strictly increasing then decreasing subsequence.

Accept integers excluding bool. Either slope may be empty. Return values of
one longest bitonic subsequence; ties choose the earliest peak and earliest
predecessor/successor found by ascending index scans. Empty input returns [].
O(n^2) time and O(n) space.

>>> longest_bitonic_subsequence([1, 3, 5, 4, 2])
[1, 3, 5, 4, 2]
"""

from algorithm_lab._validation import integer


def longest_bitonic_subsequence(values):
    values = list(values)
    for value in values:
        integer(value)
    n = len(values)
    if not n:
        return []
    up, down, previous, following = [1] * n, [1] * n, [-1] * n, [-1] * n
    for i in range(n):
        for j in range(i):
            if values[j] < values[i] and up[j] + 1 > up[i]:
                up[i], previous[i] = up[j] + 1, j
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if values[j] < values[i] and down[j] + 1 > down[i]:
                down[i], following[i] = down[j] + 1, j
    peak = max(range(n), key=lambda i: up[i] + down[i])
    left, i = [], peak
    while i != -1:
        left.append(values[i])
        i = previous[i]
    result, i = left[::-1], following[peak]
    while i != -1:
        result.append(values[i])
        i = following[i]
    return result
