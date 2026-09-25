import unittest
from itertools import product

from algorithm_lab.longest_palindromic_subsequence import longest_palindromic_subsequence


class Tests(unittest.TestCase):
    def test_exhaustive_subsequence_oracle(self):
        for n in range(8):
            for letters in product("ab", repeat=n):
                text = "".join(letters)
                subs = {
                    "".join(c for i, c in enumerate(text) if mask >> i & 1)
                    for mask in range(1 << n)
                }
                result = longest_palindromic_subsequence(text)
                self.assertIn(result, subs)
                self.assertEqual(result, result[::-1])
                self.assertEqual(len(result), max(len(s) for s in subs if s == s[::-1]))

    def test_invalid(self):
        with self.assertRaises(ValueError):
            longest_palindromic_subsequence([])
