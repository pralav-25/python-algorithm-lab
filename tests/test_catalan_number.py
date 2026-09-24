import itertools
import math
import unittest

from algorithm_lab.catalan_number import catalan_number


class CatalanTests(unittest.TestCase):
    def test_parenthesis_enumeration(self):
        for n in range(7):
            count = 0
            for steps in itertools.product([-1, 1], repeat=2 * n):
                balance, valid = 0, True
                for step in steps:
                    balance += step
                    valid &= balance >= 0
                count += valid and balance == 0
            self.assertEqual(catalan_number(n), count)
        self.assertEqual(catalan_number(300), math.comb(600, 300) // 301)

    def test_invalid(self):
        for n in [-1, True, 1.0]:
            with self.assertRaises(ValueError):
                catalan_number(n)
