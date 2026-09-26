"""Segment text into the fewest dictionary words using dynamic programming.

Return a word list, [] for empty text, or None when segmentation is impossible.
Text must be a string and dictionary entries must be nonempty strings. Ties prefer
the longest final word, recursively applying the same rule to the prefix.
Unicode code points are used without normalization. For n text characters and
maximum dictionary word length L, O(n L squared + D) time including string slices
and hashing, O(n + D) space where D is the total dictionary size.

>>> word_break('applepie', ['app', 'apple', 'le', 'pie'])
['apple', 'pie']
"""


def word_break(text, dictionary):
    if not isinstance(text, str):
        raise ValueError("text must be a string")
    words = list(dictionary)
    if any(not isinstance(word, str) or not word for word in words):
        raise ValueError("dictionary entries must be nonempty strings")
    words = set(words)
    limit = max(map(len, words), default=0)
    counts, parents = [0] + [len(text) + 1] * len(text), [-1] * (len(text) + 1)
    for stop in range(1, len(text) + 1):
        for start in range(max(0, stop - limit), stop):
            if counts[start] + 1 < counts[stop] and text[start:stop] in words:
                counts[stop], parents[stop] = counts[start] + 1, start
    if counts[-1] > len(text):
        return None
    result, stop = [], len(text)
    while stop:
        start = parents[stop]
        result.append(text[start:stop])
        stop = start
    return result[::-1]
