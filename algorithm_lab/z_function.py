"""Z[i] is the longest prefix matching text starting at i; Z[0] is defined as 0.

O(n) time and space on Unicode code points. Empty input returns []. No sentinel
characters or normalization are used.

>>> z_function('aaaa')
[0, 3, 2, 1]
"""


def z_function(text: str) -> list[int]:
    z = [0] * len(text)
    left = right = 0
    for i in range(1, len(text)):
        if i < right:
            z[i] = min(right - i, z[i - left])
        while i + z[i] < len(text) and text[z[i]] == text[i + z[i]]:
            z[i] += 1
        if i + z[i] > right:
            left, right = i, i + z[i]
    return z
