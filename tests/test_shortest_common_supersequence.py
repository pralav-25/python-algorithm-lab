import unittest
from itertools import product

from algorithm_lab.shortest_common_supersequence import shortest_common_supersequence


def subsequences(text):
    return {
        "".join(c for i, c in enumerate(text) if mask >> i & 1) for mask in range(1 << len(text))
    }


class Tests(unittest.TestCase):
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
