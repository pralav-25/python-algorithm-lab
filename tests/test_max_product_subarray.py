import unittest
from itertools import product
from math import prod

from algorithm_lab.max_product_subarray import max_product_subarray


class Tests(unittest.TestCase):
    def test_all_products(self):
        for n in range(1, 6):
            for values in product([-2, -1, 0, 2], repeat=n):
                expected = max(prod(values[i:j]) for i in range(n) for j in range(i + 1, n + 1))
                self.assertEqual(max_product_subarray(values), expected)

    def test_invalid(self):
        for values in [[], [True], [1.5]]:
            with self.assertRaises(ValueError):
                max_product_subarray(values)
