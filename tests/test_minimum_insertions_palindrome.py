import itertools
import unittest

from algorithm_lab.minimum_insertions_palindrome import minimum_insertions_palindrome


class Tests(unittest.TestCase):
    def test_palindromic_subsequence_enumeration(self):
        # Deleting n-LPS symbols and inserting their mirrors are dual operations.
        for size in range(7):
            for chars in itertools.product("ab", repeat=size):
                text = "".join(chars)
                longest = 0
                for mask in range(1 << size):
                    subsequence = "".join(text[i] for i in range(size) if mask >> i & 1)
                    if subsequence == subsequence[::-1]:
                        longest = max(longest, len(subsequence))
                self.assertEqual(minimum_insertions_palindrome(text), size - longest)
        self.assertEqual(minimum_insertions_palindrome("🙂αβ🙂"), 1)

    def test_invalid(self):
        for value in [None, [], b"a", True]:
            with self.assertRaises(ValueError):
                minimum_insertions_palindrome(value)
