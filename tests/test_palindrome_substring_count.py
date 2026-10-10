import itertools
import unittest

from algorithm_lab.palindrome_substring_count import palindrome_substring_count


class Tests(unittest.TestCase):
    def test_substring_enumeration(self):
        words = ["".join(chars) for n in range(7) for chars in itertools.product("ab", repeat=n)]
        for text in words + ["🙂α🙂", "éée"]:
            expected = sum(
                text[start:stop] == text[start:stop][::-1]
                for start in range(len(text))
                for stop in range(start + 1, len(text) + 1)
            )
            self.assertEqual(palindrome_substring_count(text), expected)

    def test_invalid(self):
        for value in [None, [], b"a", True]:
            with self.assertRaises(ValueError):
                palindrome_substring_count(value)
