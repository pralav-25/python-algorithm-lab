"""Find a longest substring occurring at least twice, allowing overlaps.

Input must be a string; characters are literal Unicode code points. Return the
substring, or an empty string when none repeats. Equal-length ties prefer the
earliest start position in the original text. O(n squared) time and O(n)
auxiliary space; the input is not changed.

>>> longest_repeated_substring('banana')
'ana'
>>> longest_repeated_substring('aaaa')
'aaa'
"""


def longest_repeated_substring(text: str) -> str:
    if not isinstance(text, str):
        raise ValueError("text must be a string")
    previous = [0] * (len(text) + 1)
    best_length, best_start = 0, 0
    for end in range(1, len(text) + 1):
        current = [0] * (len(text) + 1)
        for other_end in range(1, end):
            if text[end - 1] == text[other_end - 1]:
                length = current[other_end] = previous[other_end - 1] + 1
                start = other_end - length
                if length > best_length or (length == best_length and start < best_start):
                    best_length, best_start = length, start
        previous = current
    return text[best_start : best_start + best_length]
