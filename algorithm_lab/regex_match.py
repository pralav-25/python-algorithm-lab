"""Match an entire string against literals, dot wildcards and star repetition.

Text and pattern must be strings. Dot matches any one Unicode code point,
including newline; star repeats the preceding literal or dot zero or more times.
Leading or adjacent stars are invalid and raise ValueError. All other characters
are literals, with no escaping or normalization. Return a bool, so alternative
matching paths need no tie selection. Empty text matches an empty pattern.
O(n*m+m) time and O(m+1) space for text/pattern lengths n/m; inputs are unchanged.

>>> regex_match('aab', 'c*a*b')
True
>>> regex_match('ab', '.*c')
False
"""


def regex_match(text: str, pattern: str) -> bool:
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise ValueError("text and pattern must be strings")
    if pattern.startswith("*") or "**" in pattern:
        raise ValueError("a star must follow a literal or dot")
    previous = [True] + [False] * len(pattern)
    for column in range(2, len(pattern) + 1):
        if pattern[column - 1] == "*":
            previous[column] = previous[column - 2]
    for char in text:
        current = [False] * (len(pattern) + 1)
        for column, token in enumerate(pattern, 1):
            if token == "*":
                preceding = pattern[column - 2]
                current[column] = current[column - 2] or (
                    (preceding == "." or preceding == char) and previous[column]
                )
            else:
                current[column] = previous[column - 1] and (token == "." or token == char)
        previous = current
    return previous[-1]
