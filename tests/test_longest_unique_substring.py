import itertools
import unittest

from algorithm_lab.longest_unique_substring import longest_unique_substring


class UniqueTests(unittest.TestCase):
    def test_brute_force(self):
        for n in range(7):
            for chars in itertools.product("ab🙂", repeat=n):
                text = "".join(chars)
                candidates = [
                    text[a:b]
                    for a in range(n + 1)
                    for b in range(a, n + 1)
                    if len(set(text[a:b])) == b - a
                ]
                self.assertEqual(longest_unique_substring(text), max(candidates, key=len))
