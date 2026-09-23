"""Return all exact substring start indices using KMP in O(n + m) time.

Extra space is O(m), excluding matches. The empty pattern matches every boundary.
Python Unicode code points are compared without normalization or case folding.

>>> kmp_search('aaaa', 'aa')
[0, 1, 2]
>>> kmp_search('ab', '')
[0, 1, 2]
"""


def kmp_search(text: str, pattern: str) -> list[int]:
    if not pattern:
        return list(range(len(text) + 1))
    prefix = [0] * len(pattern)
    matched = 0
    for index in range(1, len(pattern)):
        while matched and pattern[index] != pattern[matched]:
            matched = prefix[matched - 1]
        if pattern[index] == pattern[matched]:
            matched += 1
        prefix[index] = matched
    result, matched = [], 0
    for index, char in enumerate(text):
        while matched and char != pattern[matched]:
            matched = prefix[matched - 1]
        if char == pattern[matched]:
            matched += 1
        if matched == len(pattern):
            result.append(index - len(pattern) + 1)
            matched = prefix[matched - 1]
    return result
