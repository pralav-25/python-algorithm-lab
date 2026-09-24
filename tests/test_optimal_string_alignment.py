import itertools
import unittest
from functools import lru_cache

from algorithm_lab.optimal_string_alignment import optimal_string_alignment


class OSATests(unittest.TestCase):
    def test_recursive_alignment_oracle(self):
        @lru_cache(None)
        def oracle(a, b):
            if not a or not b:
                return len(a) + len(b)
            choices = [
                1 + oracle(a[1:], b),
                1 + oracle(a, b[1:]),
                (a[0] != b[0]) + oracle(a[1:], b[1:]),
            ]
            if len(a) >= 2 and len(b) >= 2 and a[0] == b[1] and a[1] == b[0]:
                choices.append(1 + oracle(a[2:], b[2:]))
            return min(choices)

        words = ["".join(p) for n in range(5) for p in itertools.product("ab", repeat=n)]
        for a in words:
            for b in words:
                self.assertEqual(optimal_string_alignment(a, b), oracle(a, b))
        self.assertEqual(optimal_string_alignment("CA", "ABC"), 3)
        self.assertEqual(optimal_string_alignment("🙂a", "a🙂"), 1)
