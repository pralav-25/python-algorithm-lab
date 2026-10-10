"""Compute unrestricted unit-cost Damerau-Levenshtein distance.

String inputs use literal Unicode code points. Insertion, deletion, substitution
and adjacent transposition each cost one; a substring may be edited repeatedly.
Return only the minimum cost, so tied edit sequences need no selection. Inputs
are not changed. O(n*m + n + m) time and space for lengths n and m.

>>> damerau_levenshtein('CA', 'ABC')
2
>>> damerau_levenshtein('🙂a', 'a🙂')
1
"""


def damerau_levenshtein(first: str, second: str) -> int:
    if not isinstance(first, str) or not isinstance(second, str):
        raise ValueError("both inputs must be strings")
    rows, columns = len(first), len(second)
    ceiling = rows + columns
    distance = [[0] * (columns + 2) for _ in range(rows + 2)]
    distance[0][0] = ceiling
    for row in range(rows + 1):
        distance[row + 1][0] = ceiling
        distance[row + 1][1] = row
    for column in range(columns + 1):
        distance[0][column + 1] = ceiling
        distance[1][column + 1] = column
    last_row = {}
    for row, char in enumerate(first, 1):
        last_match = 0
        for column, other in enumerate(second, 1):
            previous_row = last_row.get(other, 0)
            previous_column = last_match
            cost = int(char != other)
            if not cost:
                last_match = column
            distance[row + 1][column + 1] = min(
                distance[row][column] + cost,
                distance[row + 1][column] + 1,
                distance[row][column + 1] + 1,
                distance[previous_row][previous_column]
                + row
                - previous_row
                - 1
                + 1
                + column
                - previous_column
                - 1,
            )
        last_row[char] = row
    return distance[rows + 1][columns + 1]
