"""Decide whether a string interleaves two strings in their original order.

All arguments must be strings. Each source character must be used exactly once;
Unicode code points match literally. Return a bool; alternative interleavings
need no tie selection. Empty sources interleave to the empty result. O(n*m+n+m)
time and O(m+1) auxiliary space for source lengths n and m; inputs are unchanged.

>>> interleaving_strings('ab', 'cd', 'acbd')
True
>>> interleaving_strings('ab', 'cd', 'adbc')
False
"""


def interleaving_strings(first: str, second: str, result: str) -> bool:
    if any(not isinstance(value, str) for value in (first, second, result)):
        raise ValueError("all inputs must be strings")
    if len(result) != len(first) + len(second):
        return False
    possible = [True] + [False] * len(second)
    for column in range(1, len(second) + 1):
        possible[column] = possible[column - 1] and second[column - 1] == result[column - 1]
    for row, char in enumerate(first, 1):
        possible[0] = possible[0] and char == result[row - 1]
        for column, other in enumerate(second, 1):
            target = result[row + column - 1]
            possible[column] = (possible[column] and char == target) or (
                possible[column - 1] and other == target
            )
    return possible[-1]
