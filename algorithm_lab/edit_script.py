"""Reconstruct a minimum-cost Levenshtein alignment.

Accept two strings and return (distance, operations). Each operation is
(kind, source_character, target_character), using '' for absent characters.
Kinds are equal, replace, delete, insert. Unit-cost ties prefer diagonal,
then deletion, then insertion. Unicode code points are not normalized.
O(len(source)*len(target)) time and space.

>>> edit_script('cat', 'cut')
(1, [('equal', 'c', 'c'), ('replace', 'a', 'u'), ('equal', 't', 't')])
"""


def edit_script(source, target):
    if not isinstance(source, str) or not isinstance(target, str):
        raise ValueError("inputs must be strings")
    m, n = len(source), len(target)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = min(
                dp[i - 1][j] + 1,
                dp[i][j - 1] + 1,
                dp[i - 1][j - 1] + (source[i - 1] != target[j - 1]),
            )
    i, j, operations = m, n, []
    while i or j:
        if i and j and dp[i][j] == dp[i - 1][j - 1] + (source[i - 1] != target[j - 1]):
            operations.append(
                (
                    "equal" if source[i - 1] == target[j - 1] else "replace",
                    source[i - 1],
                    target[j - 1],
                )
            )
            i, j = i - 1, j - 1
        elif i and dp[i][j] == dp[i - 1][j] + 1:
            operations.append(("delete", source[i - 1], ""))
            i -= 1
        else:
            operations.append(("insert", "", target[j - 1]))
            j -= 1
    return dp[m][n], operations[::-1]
