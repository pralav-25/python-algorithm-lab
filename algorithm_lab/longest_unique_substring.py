"""Return the earliest longest substring with distinct Unicode code points.

O(n) expected time and O(min(n, alphabet size)) space, excluding output.
No normalization is performed. Empty text returns an empty string.

>>> longest_unique_substring('abba')
'ab'
"""


def longest_unique_substring(text: str) -> str:
    seen = {}
    start = best_start = best_length = 0
    for end, char in enumerate(text):
        start = max(start, seen.get(char, -1) + 1)
        seen[char] = end
        if end - start + 1 > best_length:
            best_start, best_length = start, end - start + 1
    return text[best_start : best_start + best_length]
