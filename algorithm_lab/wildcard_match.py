"""Match the entire text: ? means one code point, * means zero or more.

All other characters (including brackets and backslash) are literal; no escape
syntax. O(n*m) time, O(m) space for text length n and pattern length m.

>>> wildcard_match('report.csv', '*.csv')
True
>>> wildcard_match('ab', 'a?c')
False
"""


def wildcard_match(text: str, pattern: str) -> bool:
    previous = [True] + [False] * len(pattern)
    for j, token in enumerate(pattern, 1):
        previous[j] = token == "*" and previous[j - 1]
    for char in text:
        current = [False] * (len(pattern) + 1)
        for j, token in enumerate(pattern, 1):
            if token == "*":
                current[j] = current[j - 1] or previous[j]
            else:
                current[j] = previous[j - 1] and (token == "?" or token == char)
        previous = current
    return previous[-1]
