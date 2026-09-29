import unittest
from itertools import product

from algorithm_lab.longest_palindromic_subsequence import longest_palindromic_subsequence


class Tests(unittest.TestCase):
    def test_right_endpoint_is_dropped_on_equal_lengths(self):
        for text, expected in [("abc", "a"), ("abca", "aba"), ("bbab", "bbb"), ("🙂a🙂b", "🙂a🙂")]:
            with self.subTest(text=text):
                self.assertEqual(longest_palindromic_subsequence(text), expected)

    def test_unicode_is_not_normalized_before_palindrome_search(self):
        self.assertEqual(longest_palindromic_subsequence("ée\u0301"), "é")
        self.assertEqual(longest_palindromic_subsequence("e\u0301e"), "e\u0301e")

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
