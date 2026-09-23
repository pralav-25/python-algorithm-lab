import itertools
import unittest

from algorithm_lab.balanced_brackets import balanced_brackets


class BracketTests(unittest.TestCase):
    def test_reduction_oracle(self):
        for size in range(7):
            for chars in itertools.product("()[]", repeat=size):
                text = "".join(chars)
                reduced = text
                while True:
                    shorter = reduced.replace("()", "").replace("[]", "")
                    if shorter == reduced:
                        break
                    reduced = shorter
                self.assertEqual(balanced_brackets(text), not reduced)

    def test_ignored_characters_and_unmatched_braces(self):
        self.assertTrue(balanced_brackets("x{a[b(c)]}y"))
        self.assertFalse(balanced_brackets("}"))
        self.assertFalse(balanced_brackets("{{}"))
        self.assertTrue(balanced_brackets("ordinary text"))
