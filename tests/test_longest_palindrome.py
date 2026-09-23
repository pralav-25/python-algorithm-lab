import itertools
import unittest

from algorithm_lab.longest_palindrome import longest_palindrome


class PalindromeTests(unittest.TestCase):
    def test_all_substrings_oracle(self):
        for size in range(8):
            for chars in itertools.product("ab", repeat=size):
                text = "".join(chars)
                options = [
                    text[i:j]
                    for i in range(size + 1)
                    for j in range(i, size + 1)
                    if text[i:j] == text[i:j][::-1]
                ]
                expected = max(options, key=len)
                self.assertEqual(longest_palindrome(text), expected)

    def test_unicode_and_even_center(self):
        self.assertEqual(longest_palindrome("a🙂🙂b"), "🙂🙂")
        self.assertEqual(longest_palindrome("babad"), "bab")
