"""Return one longest common subsequence, not necessarily a contiguous substring.

Time and space are O(nm). On equal-length traceback choices, reduce the first
string's position first. The result is deterministic, not necessarily lexicographic.

>>> longest_common_subsequence('abc', 'ac')
'ac'
"""


def longest_common_subsequence(first: str, second: str) -> str:
    table = [[0] * (len(second) + 1) for _ in range(len(first) + 1)]
    for i, left in enumerate(first, 1):
        for j, right in enumerate(second, 1):
            table[i][j] = (
                table[i - 1][j - 1] + 1 if left == right else max(table[i - 1][j], table[i][j - 1])
            )
    i, j, result = len(first), len(second), []
    while i and j:
        if first[i - 1] == second[j - 1]:
            result.append(first[i - 1])
            i, j = i - 1, j - 1
        elif table[i - 1][j] >= table[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return "".join(reversed(result))
