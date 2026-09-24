"""Return the earliest longest palindromic substring in O(n) time and space.

Manacher's algorithm keeps odd/even radii without reserved sentinel characters.
Unicode code points are compared exactly; empty text returns ''.

>>> manacher('babad')
'bab'
>>> manacher('cbbd')
'bb'
"""


def manacher(text: str) -> str:
    n = len(text)
    best_start = best_length = 0
    for parity in (1, 0):
        radius = [0] * n
        left, right = 0, -1
        for i in range(n):
            k = parity if i > right else min(radius[left + right - i + 1 - parity], right - i + 1)
            while i - k >= 1 - parity and i + k < n and text[i - k - 1 + parity] == text[i + k]:
                k += 1
            radius[i] = k
            start, length = i - k + parity, 2 * k - parity
            if length > best_length or (length == best_length and start < best_start):
                best_start, best_length = start, length
            if i + k - 1 > right:
                left, right = start, i + k - 1
    return text[best_start : best_start + best_length]
