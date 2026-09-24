"""Return the earliest shortest substring containing every required code point.

Multiplicities matter. Empty requirement or no cover returns ''. O(n+m) expected
time and O(m) space, excluding output, for text/requirement lengths n/m.

>>> minimum_window('ADOBECODEBANC', 'ABC')
'BANC'
"""

from collections import Counter


def minimum_window(text: str, required: str) -> str:
    if not required:
        return ""
    need = Counter(required)
    missing, left = len(required), 0
    best_start, best_length = 0, len(text) + 1
    for right, char in enumerate(text, 1):
        if char in need:
            missing -= need[char] > 0
            need[char] -= 1
        while missing == 0:
            if right - left < best_length:
                best_start, best_length = left, right - left
            outgoing = text[left]
            if outgoing in need:
                need[outgoing] += 1
                missing += need[outgoing] > 0
            left += 1
    return "" if best_length > len(text) else text[best_start : best_start + best_length]
