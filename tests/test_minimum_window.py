import itertools
import unittest
from collections import Counter

from algorithm_lab.minimum_window import minimum_window


class WindowTests(unittest.TestCase):
    def test_exhaustive(self):
        for n in range(7):
            for chars in itertools.product("ab", repeat=n):
                text = "".join(chars)
                for required in ["", "a", "b", "aa", "ab", "aab", "c"]:
                    candidates = [
                        text[a:b]
                        for a in range(n + 1)
                        for b in range(a, n + 1)
                        if not Counter(required) - Counter(text[a:b])
                    ]
                    expected = min(candidates, key=len, default="")
                    self.assertEqual(minimum_window(text, required), expected)
        self.assertEqual(minimum_window("x🙂a🙂y", "🙂🙂"), "🙂a🙂")
