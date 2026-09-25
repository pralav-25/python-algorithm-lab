"""Count distinct subsequence strings including the empty string.

Accept a Unicode string without normalization. Repeated characters share a
last-contribution count to avoid counting identical strings twice. Return an
exact integer. O(n) dictionary operations and O(number of distinct characters)
stored integers; arithmetic cost grows with the result's bit length.

>>> count_distinct_subsequences('aba')
7
"""


def count_distinct_subsequences(text):
    if not isinstance(text, str):
        raise ValueError("input must be a string")
    total, last = 1, {}
    for character in text:
        total, last[character] = 2 * total - last.get(character, 0), total
    return total
