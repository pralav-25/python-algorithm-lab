import unittest
from itertools import product

from algorithm_lab.count_distinct_subsequences import count_distinct_subsequences


class Tests(unittest.TestCase):
    def test_set_oracle(self):
        for n in range(8):
            for text in product("ab", repeat=n):
                expected = {
                    tuple(c for i, c in enumerate(text) if mask >> i & 1) for mask in range(1 << n)
                }
                self.assertEqual(count_distinct_subsequences("".join(text)), len(expected))
        self.assertEqual(count_distinct_subsequences("x" * 2000), 2001)

    def test_invalid(self):
        with self.assertRaises(ValueError):
            count_distinct_subsequences([])
