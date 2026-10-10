import itertools
import unittest

from algorithm_lab.longest_repeated_substring import longest_repeated_substring


class Tests(unittest.TestCase):
    def test_all_substring_candidates(self):
        words = ["".join(chars) for n in range(7) for chars in itertools.product("ab", repeat=n)]
        for text in words + ["banana", "🙂α🙂α🙂", "abXabYcdZcd", "xyz"]:
            candidates = [
                (stop - start, start, text[start:stop])
                for start in range(len(text))
                for stop in range(start + 1, len(text) + 1)
                if text.find(text[start:stop], start + 1) >= 0
            ]
            expected = (
                min(candidates, key=lambda item: (-item[0], item[1]))[2] if candidates else ""
            )
            self.assertEqual(longest_repeated_substring(text), expected)
        self.assertEqual(longest_repeated_substring("aaaa"), "aaa")
        self.assertEqual(longest_repeated_substring("abXabYcdZcd"), "ab")

    def test_invalid(self):
        for value in [None, [], b"a", True]:
            with self.assertRaises(ValueError):
                longest_repeated_substring(value)
