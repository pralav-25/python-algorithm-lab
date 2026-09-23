"""Return all overlapping exact matches using a rolling polynomial hash.

Empty patterns match all boundaries. Hash hits are verified against actual text,
so collisions cannot create false matches. Time is O(n + m) plus O(m) per hash
hit (O(nm) worst case); auxiliary space is O(m) for verification slices.

>>> rabin_karp('banana', 'ana')
[1, 3]
"""


def rabin_karp(text: str, pattern: str) -> list[int]:
    size = len(pattern)
    if not size:
        return list(range(len(text) + 1))
    if size > len(text):
        return []
    base, modulus = 257, 1_000_000_007
    high = pow(base, size - 1, modulus)
    target = current = 0
    for index in range(size):
        target = (target * base + ord(pattern[index])) % modulus
        current = (current * base + ord(text[index])) % modulus
    matches = []
    for start in range(len(text) - size + 1):
        if current == target and text[start : start + size] == pattern:
            matches.append(start)
        if start + size < len(text):
            current = (
                (current - ord(text[start]) * high) * base + ord(text[start + size])
            ) % modulus
    return matches
