import itertools
import unittest

from algorithm_lab.boyer_moore_horspool import boyer_moore_horspool


class Tests(unittest.TestCase):
    def test_exhaustive_slice_oracle(self):
        words = ["".join(chars) for n in range(5) for chars in itertools.product("ab", repeat=n)]
        for text in words + ["🙂a🙂a🙂", "ééé"]:
            for pattern in words + ["🙂a", "é", "x"]:
                expected = [
                    start
                    for start in range(len(text) + 1)
                    if text[start : start + len(pattern)] == pattern
                ]
                self.assertEqual(boyer_moore_horspool(text, pattern), expected)

    def test_invalid_types(self):
        for text, pattern in [(None, ""), ("", []), (b"a", "a"), (True, "")]:
            with self.assertRaises(ValueError):
                boyer_moore_horspool(text, pattern)
