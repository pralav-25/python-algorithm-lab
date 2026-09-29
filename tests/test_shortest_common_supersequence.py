import unittest
from itertools import product

from algorithm_lab.shortest_common_supersequence import shortest_common_supersequence


def subsequences(text):
    return {
        "".join(c for i, c in enumerate(text) if mask >> i & 1) for mask in range(1 << len(text))
    }


class Tests(unittest.TestCase):
    def test_first_string_ties_and_unicode_suffixes(self):
        for left, right, expected in [
            ("ab", "ba", "aba"),
            ("ba", "ab", "bab"),
            ("🙂a", "🙂b", "🙂ab"),
            ("é", "e\u0301", "ée\u0301"),
            ("", "🙂e\u0301", "🙂e\u0301"),
            ("🙂e\u0301", "", "🙂e\u0301"),
            ("🙂🙂", "🙂", "🙂🙂"),
        ]:
            with self.subTest(left=left, right=right):
                self.assertEqual(shortest_common_supersequence(left, right), expected)

    def test_exhaustive_length_and_witness(self):
        words = ["".join(p) for n in range(4) for p in product("ab", repeat=n)]
        for a in words:
            for b in words:
                result = shortest_common_supersequence(a, b)
                lcs = max(map(len, subsequences(a) & subsequences(b)))
                self.assertEqual(len(result), len(a) + len(b) - lcs)
                self.assertIn(a, subsequences(result))
                self.assertIn(b, subsequences(result))

    def test_invalid(self):
        with self.assertRaises(ValueError):
            shortest_common_supersequence("", [])
