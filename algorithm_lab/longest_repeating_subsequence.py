"""Return the length of a subsequence repeated at distinct aligned indices.

The input must be a string; matching uses literal Unicode code points. Two
subsequence occurrences may share indices, but each aligned pair must use
different positions. Empty input returns zero. No subsequence is reconstructed,
so ties need no selection. O(n squared) time, O(n) space; no input mutation.

>>> longest_repeating_subsequence('aabebcdd')
3
"""


def longest_repeating_subsequence(text: str) -> int:
    if not isinstance(text, str):
        raise ValueError("text must be a string")
    previous = [0] * (len(text) + 1)
    for row, char in enumerate(text, 1):
        current = [0] * (len(text) + 1)
        for column, other in enumerate(text, 1):
            if row != column and char == other:
                current[column] = previous[column - 1] + 1
            else:
                current[column] = max(previous[column], current[column - 1])
        previous = current
    return previous[-1]
