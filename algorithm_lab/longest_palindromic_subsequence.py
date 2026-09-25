"""Reconstruct a longest palindromic subsequence.

Accept a string and return one longest palindromic subsequence. When dropping
either endpoint yields the same length, drop the right endpoint. Empty input
returns ''. Operates on Unicode code points; O(n^2) time and space.

>>> longest_palindromic_subsequence('bbbab')
'bbbb'
"""


def longest_palindromic_subsequence(text):
    if not isinstance(text, str):
        raise ValueError("input must be a string")
    n = len(text)
    if not n:
        return ""
    dp = [[0] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        dp[i][i] = 1
        for j in range(i + 1, n):
            dp[i][j] = (
                2 + dp[i + 1][j - 1] if text[i] == text[j] else max(dp[i + 1][j], dp[i][j - 1])
            )
    i, j, left, right = 0, n - 1, [], []
    while i <= j:
        if i == j:
            left.append(text[i])
            break
        if text[i] == text[j]:
            left.append(text[i])
            right.append(text[j])
            i, j = i + 1, j - 1
        elif dp[i][j - 1] >= dp[i + 1][j]:
            j -= 1
        else:
            i += 1
    return "".join(left + right[::-1])
