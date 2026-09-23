"""Unit-cost insert/delete/substitute edit distance between Unicode strings.

Time O(nm), working space O(min(n, m)); transpositions are not one operation.
Code points are compared exactly, with no normalization or case folding.

>>> levenshtein('kitten', 'sitting')
3
"""


def levenshtein(first: str, second: str) -> int:
    if len(first) < len(second):
        first, second = second, first
    previous = list(range(len(second) + 1))
    for row, left in enumerate(first, 1):
        current = [row]
        for column, right in enumerate(second, 1):
            current.append(
                min(current[-1] + 1, previous[column] + 1, previous[column - 1] + (left != right))
            )
        previous = current
    return previous[-1]
