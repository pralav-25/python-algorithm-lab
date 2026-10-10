"""Count nonempty palindromic substrings by their start and end positions.

The input must be a string; Unicode code points match literally. Repeated equal
substrings at different positions are counted separately. Empty text gives zero.
All occurrences are counted, so ties need no selection. O(n squared) worst-case
time and O(1) auxiliary space; the input is not changed.

>>> palindrome_substring_count('aaa')
6
"""


def palindrome_substring_count(text: str) -> int:
    if not isinstance(text, str):
        raise ValueError("text must be a string")
    total = 0
    for center in range(2 * len(text) - 1):
        left, right = center // 2, (center + 1) // 2
        while left >= 0 and right < len(text) and text[left] == text[right]:
            total += 1
            left -= 1
            right += 1
    return total
