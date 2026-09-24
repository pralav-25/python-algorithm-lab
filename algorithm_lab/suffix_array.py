"""Indices of nonempty suffixes in lexicographic order of Unicode code points.

Prefix doubling with comparison sorting takes O(n log² n) time and O(n) working
space. Empty text returns []. No sentinel is appended and input is unchanged.

>>> suffix_array('banana')
[5, 3, 1, 0, 4, 2]
"""


def suffix_array(text: str) -> list[int]:
    n = len(text)
    order = list(range(n))
    ranks = [ord(char) for char in text]
    width = 1
    while width < n:
        order.sort(key=lambda i: (ranks[i], ranks[i + width] if i + width < n else -1))
        updated = [0] * n
        for position in range(1, n):
            a, b = order[position - 1], order[position]
            first = (ranks[a], ranks[a + width] if a + width < n else -1)
            second = (ranks[b], ranks[b + width] if b + width < n else -1)
            updated[b] = updated[a] + (first != second)
        ranks = updated
        if ranks[order[-1]] == n - 1:
            break
        width *= 2
    return order
