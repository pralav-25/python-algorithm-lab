"""Reconstruct a shortest string containing two subsequences.

Inputs are strings of Unicode code points without normalization. Return a
shortest common supersequence, preferring a character from the first string
on equal remaining lengths. O(m*n) time and space, plus output length.

>>> shortest_common_supersequence('ab', 'ac')
'abc'
"""


def shortest_common_supersequence(left, right):
    if not isinstance(left, str) or not isinstance(right, str):
        raise ValueError("inputs must be strings")
    m, n = len(left), len(right)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m, -1, -1):
        for j in range(n, -1, -1):
            if i == m:
                dp[i][j] = n - j
            elif j == n:
                dp[i][j] = m - i
            elif left[i] == right[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1])
    i, j, result = 0, 0, []
    while i < m and j < n:
        if left[i] == right[j]:
            result.append(left[i])
            i, j = i + 1, j + 1
        elif dp[i + 1][j] <= dp[i][j + 1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return "".join(result) + left[i:] + right[j:]
