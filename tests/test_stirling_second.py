import itertools
import math
import unittest

from algorithm_lab.stirling_second import stirling_second


class Tests(unittest.TestCase):
    def test_surjection_oracle(self):
        for n in range(7):
            for k in range(5):
                onto = sum(
                    len(set(values)) == k for values in itertools.product(range(k), repeat=n)
                )
                self.assertEqual(stirling_second(n, k), onto // math.factorial(k))

    def test_invalid(self):
        for args in [(-1, 1), (1, -1), (True, 1), (1, 1.5)]:
            with self.assertRaises(ValueError):
                stirling_second(*args)
