"""Find exact substring matches using Sunday's look-ahead shifts.

Text and pattern must be strings. Return all start indices in ascending order,
including overlaps. An empty pattern matches every boundary. Unicode code points
are literal, with no normalization. O(n*m) worst-case time and O(m) auxiliary
space excluding output, for lengths n and m. Inputs are not changed.

>>> sunday_search('aaaa', 'aa')
[0, 1, 2]
"""


def sunday_search(text: str, pattern: str) -> list[int]:
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise ValueError("text and pattern must be strings")
    size = len(pattern)
    if not size:
        return list(range(len(text) + 1))
    shifts = {char: size - index for index, char in enumerate(pattern)}
    result, start = [], 0
    while start + size <= len(text):
        if text.startswith(pattern, start):
            result.append(start)
        if start + size == len(text):
            break
        start += shifts.get(text[start + size], size + 1)
    return result
