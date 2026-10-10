"""Find exact substring matches with Boyer-Moore-Horspool shifts.

Both arguments must be strings. Return ascending start indices, including
overlaps; an empty pattern matches every boundary. Unicode code points are
compared literally. O(n*m) worst-case time and O(m) auxiliary space excluding
matches, for text length n and pattern length m. Inputs are not changed.

>>> boyer_moore_horspool('bananana', 'ana')
[1, 3, 5]
"""


def boyer_moore_horspool(text: str, pattern: str) -> list[int]:
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise ValueError("text and pattern must be strings")
    size = len(pattern)
    if not size:
        return list(range(len(text) + 1))
    shifts = {char: size - 1 - index for index, char in enumerate(pattern[:-1])}
    matches, start = [], 0
    while start + size <= len(text):
        index = size - 1
        while index >= 0 and text[start + index] == pattern[index]:
            index -= 1
        if index < 0:
            matches.append(start)
        start += shifts.get(text[start + size - 1], size)
    return matches
