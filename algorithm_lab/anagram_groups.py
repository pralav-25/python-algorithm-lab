"""Group anagrams, preserving first group appearance and word order within groups.

Words are strings compared as Unicode code points, case-sensitively without
normalization. Duplicates and empty words are retained. O(sum(k log k)) time
for word lengths k, O(total characters) auxiliary key storage.

>>> anagram_groups(['eat', 'tea', 'bat', 'ate'])
[['eat', 'tea', 'ate'], ['bat']]
"""


def anagram_groups(words):
    groups = {}
    for word in words:
        if not isinstance(word, str):
            raise ValueError("words must be strings")
        groups.setdefault("".join(sorted(word)), []).append(word)
    return list(groups.values())
