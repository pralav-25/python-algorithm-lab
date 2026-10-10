"""Return the fewest inserted characters needed to make a palindrome.

The input must be a string, compared as literal Unicode code points. Existing
characters keep their order; insertions may occur anywhere. Empty input returns
zero. Only the minimum count is returned, so tied palindromes need no selection.
O(n squared) time and O(n) space; the input is not changed.

>>> minimum_insertions_palindrome('mbadm')
2
"""


def minimum_insertions_palindrome(text: str) -> int:
    if not isinstance(text, str):
        raise ValueError("text must be a string")
    costs = [0] * len(text)
    for start in range(len(text) - 2, -1, -1):
        diagonal = 0
        for end in range(start + 1, len(text)):
            old = costs[end]
            costs[end] = (
                diagonal if text[start] == text[end] else 1 + min(costs[end], costs[end - 1])
            )
            diagonal = old
    return costs[-1] if costs else 0
