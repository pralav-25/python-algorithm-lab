import math
import unittest

from algorithm_lab.pascal_row import pascal_row


class PascalTests(unittest.TestCase):
    def test_combinations_and_identities(self):
        for n in range(150):
            row = pascal_row(n)
            self.assertEqual(row, [math.comb(n, k) for k in range(n + 1)])
            self.assertEqual(sum(row), 2**n)
            self.assertEqual(row, row[::-1])

    def test_invalid(self):
        for n in [-1, False, 1.2]:
            with self.assertRaises(ValueError):
                pascal_row(n)
