"""Aho-Corasick automaton for nonempty string patterns, including duplicates.

find_all returns (start, stop, pattern_index) tuples with half-open offsets.
Matches are ordered by end offset; ties have no promised ordering. Empty pattern
lists are valid; empty/non-string patterns raise ValueError. Unicode is exact.
For total pattern length S, maximum length L, inherited output count Q: building
uses O(S*L+Q) time conservatively and O(S+Q) space. Search O(n+matches).

>>> matcher = AhoCorasick(['he', 'she', 'hers'])
>>> sorted(matcher.find_all('ushers'))
[(1, 4, 1), (2, 4, 0), (2, 6, 2)]
"""

from collections import deque


class AhoCorasick:
    def __init__(self, patterns):
        patterns = list(patterns)
        if any(not isinstance(p, str) or not p for p in patterns):
            raise ValueError("patterns must be nonempty strings")
        self._lengths = [len(p) for p in patterns]
        self._next, self._fail, self._output = [{}], [0], [[]]
        for pattern_id, pattern in enumerate(patterns):
            state = 0
            for char in pattern:
                if char not in self._next[state]:
                    self._next[state][char] = len(self._next)
                    self._next.append({})
                    self._fail.append(0)
                    self._output.append([])
                state = self._next[state][char]
            self._output[state].append(pattern_id)
        queue = deque(self._next[0].values())
        while queue:
            state = queue.popleft()
            for char, child in self._next[state].items():
                queue.append(child)
                fallback = self._fail[state]
                while fallback and char not in self._next[fallback]:
                    fallback = self._fail[fallback]
                self._fail[child] = self._next[fallback].get(char, 0)
                self._output[child].extend(self._output[self._fail[child]])

    def find_all(self, text):
        state, matches = 0, []
        for stop, char in enumerate(text, 1):
            while state and char not in self._next[state]:
                state = self._fail[state]
            state = self._next[state].get(char, 0)
            for pattern_id in self._output[state]:
                matches.append((stop - self._lengths[pattern_id], stop, pattern_id))
        return matches
