import itertools
import unittest

from algorithm_lab.longest_valid_parentheses import longest_valid_parentheses


class Tests(unittest.TestCase):
    def test_exhaustive_substring_oracle(self):
        for n in range(10):
            for chars in itertools.product("()", repeat=n):
                text, expected = "".join(chars), (0, 0)
                for start in range(n):
                    balance = 0
                    for stop in range(start, n):
                        balance += 1 if text[stop] == "(" else -1
                        if balance < 0:
                            break
                        if balance == 0 and stop + 1 - start > expected[1] - expected[0]:
                            expected = (start, stop + 1)
                self.assertEqual(longest_valid_parentheses(text), expected)

    def test_invalid(self):
        for text in ["a", "( )", None, ["("]]:
            with self.assertRaises(ValueError):
                longest_valid_parentheses(text)
