import math
import unittest

from algorithm_lab.binomial_coefficient import binomial_coefficient as choose


class BinomialTests(unittest.TestCase):
    def test_math_comb_and_row_sums(self):
        for n in range(70):
            for k in range(n + 3):
                self.assertEqual(choose(n, k), math.comb(n, k))
            self.assertEqual(sum(choose(n, k) for k in range(n + 1)), 2**n)
        self.assertEqual(choose(1000, 500), math.comb(1000, 500))

    def test_pascal_identity_and_invalid_inputs(self):
        for n in range(1, 30):
            for k in range(1, n):
                self.assertEqual(choose(n, k), choose(n - 1, k - 1) + choose(n - 1, k))
        for n, k in [(-1, 0), (1, -1), (True, 1), (2, 1.5)]:
            with self.assertRaises(ValueError):
                choose(n, k)
