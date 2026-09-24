"""Unit-cost insertion, deletion, substitution and adjacent transposition distance.

This is restricted Damerau-Levenshtein (optimal string alignment): a substring
cannot be edited twice. It is not unrestricted Damerau-Levenshtein distance.
O(len(a)*len(b)) time/space on Unicode code points.

>>> optimal_string_alignment('ca', 'ac')
1
>>> optimal_string_alignment('CA', 'ABC')
3
"""


def optimal_string_alignment(first: str, second: str) -> int:
    rows, cols = len(first), len(second)
    dp = [[0] * (cols + 1) for _ in range(rows + 1)]
    for i in range(rows + 1):
        dp[i][0] = i
    for j in range(cols + 1):
        dp[0][j] = j
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            dp[i][j] = min(
                dp[i - 1][j] + 1,
                dp[i][j - 1] + 1,
                dp[i - 1][j - 1] + (first[i - 1] != second[j - 1]),
            )
            if i > 1 and j > 1 and first[i - 1] == second[j - 2] and first[i - 2] == second[j - 1]:
                dp[i][j] = min(dp[i][j], dp[i - 2][j - 2] + 1)
    return dp[rows][cols]
