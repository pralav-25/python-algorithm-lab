"""Split text into the fewest palindromic substrings; empty text returns [].

O(n²) time/space. Equal-cost transitions prefer the earliest start of the final
piece, recursively under the same rule. Unicode code points are compared exactly.

>>> palindrome_partition('aab')
['aa', 'b']
"""


def palindrome_partition(text: str) -> list[str]:
    n = len(text)
    pal = [[False] * n for _ in range(n)]
    for left in range(n - 1, -1, -1):
        for right in range(left, n):
            pal[left][right] = text[left] == text[right] and (
                right - left < 2 or pal[left + 1][right - 1]
            )
    cost, previous = [0] + [n + 1] * n, [0] * (n + 1)
    for stop in range(1, n + 1):
        for start in range(stop):
            if pal[start][stop - 1] and cost[start] + 1 < cost[stop]:
                cost[stop], previous[stop] = cost[start] + 1, start
    parts, stop = [], n
    while stop:
        start = previous[stop]
        parts.append(text[start:stop])
        stop = start
    return parts[::-1]
