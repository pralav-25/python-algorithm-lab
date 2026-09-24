import itertools
import unittest

from algorithm_lab.manacher import manacher


class ManacherTests(unittest.TestCase):
    def test_all_small_strings(self):
        for n in range(9):
            for chars in itertools.product("a#", repeat=n):
                text = "".join(chars)
                candidates = [
                    text[a:b]
                    for a in range(n + 1)
                    for b in range(a, n + 1)
                    if text[a:b] == text[a:b][::-1]
                ]
                self.assertEqual(manacher(text), max(candidates, key=len))
        self.assertEqual(manacher("🙂a🙂"), "🙂a🙂")
        self.assertEqual(manacher("x" * 20000), "x" * 20000)
