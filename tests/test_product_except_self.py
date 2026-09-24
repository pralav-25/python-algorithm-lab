import itertools
import math
import unittest

from algorithm_lab.product_except_self import product_except_self


class ProductTests(unittest.TestCase):
    def test_exhaustive(self):
        for n in range(6):
            for data in itertools.product([-2, 0, 3], repeat=n):
                expected = [math.prod(data[:i] + data[i + 1 :]) for i in range(n)]
                self.assertEqual(product_except_self(iter(data)), expected)
        with self.assertRaises(ValueError):
            product_except_self([True])
