"""Count segmentations of text into dictionary words.

Text must be a string; dictionary is an iterable of nonempty strings. Duplicate
words are deduplicated, and literal Unicode comparison is used. Empty text has
one empty segmentation. Return an exact count, counting all tied choices. Inputs
are not changed. O(n*(L+1) squared + D) time including slicing/hashing, O(n + D) space,
where L is maximum word length and D is the total dictionary size.

>>> word_break_count('aaaa', ['a', 'aa', 'aa'])
5
"""


def word_break_count(text: str, dictionary) -> int:
    if not isinstance(text, str):
        raise ValueError("text must be a string")
    words = list(dictionary)
    if any(not isinstance(word, str) or not word for word in words):
        raise ValueError("dictionary entries must be nonempty strings")
    words = set(words)
    limit = max(map(len, words), default=0)
    counts = [1] + [0] * len(text)
    for stop in range(1, len(text) + 1):
        counts[stop] = sum(
            counts[start]
            for start in range(max(0, stop - limit), stop)
            if text[start:stop] in words
        )
    return counts[-1]
