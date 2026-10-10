import itertools
import unittest
from collections import deque

from algorithm_lab.damerau_levenshtein import damerau_levenshtein


class Tests(unittest.TestCase):
    @staticmethod
    def edit_graph(source, alphabet="ab"):
        # With both endpoints at most two characters, a shortest path needs at
        # most two edits. BFS independently enumerates actual edit operations.
        distances, queue = {source: 0}, deque([source])
        while queue:
            text = queue.popleft()
            distance = distances[text]
            if distance == 2:
                continue
            neighbors = set()
            for index in range(len(text)):
                neighbors.add(text[:index] + text[index + 1 :])
                for char in alphabet:
                    neighbors.add(text[:index] + char + text[index + 1 :])
            for index in range(len(text) + 1):
                for char in alphabet:
                    neighbors.add(text[:index] + char + text[index:])
            for index in range(len(text) - 1):
                neighbors.add(text[:index] + text[index + 1] + text[index] + text[index + 2 :])
            for neighbor in neighbors:
                if neighbor not in distances:
                    distances[neighbor] = distance + 1
                    queue.append(neighbor)
        return distances

    def test_edit_operation_bfs(self):
        words = ["".join(chars) for n in range(3) for chars in itertools.product("ab", repeat=n)]
        for first in words:
            expected = self.edit_graph(first)
            for second in words:
                self.assertEqual(damerau_levenshtein(first, second), expected[second])

    def test_unrestricted_and_unicode(self):
        # Swap CA to AC, then insert B inside the already edited substring.
        self.assertEqual(damerau_levenshtein("CA", "ABC"), self.edit_graph("CA", "ABC")["ABC"])
        self.assertEqual(damerau_levenshtein("ABC", "CA"), 2)
        self.assertEqual(damerau_levenshtein("🙂a", "a🙂"), 1)
        self.assertEqual(damerau_levenshtein("", "αβγ"), 3)
        self.assertEqual(damerau_levenshtein("abca", "abca"), 0)

    def test_invalid(self):
        for first, second in [(None, ""), ("", []), (b"a", "a")]:
            with self.assertRaises(ValueError):
                damerau_levenshtein(first, second)
