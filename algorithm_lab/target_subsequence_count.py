"""Count index selections whose characters form a target subsequence.

Both inputs must be strings, compared by literal Unicode code points. Equal
characters at different source indices give distinct selections. The empty
target counts once, even in empty text. Return an exact integer; all choices
are counted, so ties need no selection. O(n*m+n+m) time and O(m+1) space for source
length n and target length m, excluding integer arithmetic; inputs are unchanged.

>>> target_subsequence_count('rabbbit', 'rabbit')
3
"""


def target_subsequence_count(text: str, target: str) -> int:
    if not isinstance(text, str) or not isinstance(target, str):
        raise ValueError("text and target must be strings")
    counts = [1] + [0] * len(target)
    for char in text:
        for size in range(len(target), 0, -1):
            if char == target[size - 1]:
                counts[size] += counts[size - 1]
    return counts[-1]
