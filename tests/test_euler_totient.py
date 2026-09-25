import math
import unittest

from algorithm_lab.euler_totient import euler_totient


class Tests(unittest.TestCase):
    def test_count_oracle(self):
        for n in range(1, 400):
            self.assertEqual(euler_totient(n), sum(math.gcd(n, k) == 1 for k in range(1, n + 1)))

    def test_invalid(self):
        for n in [0, -1, True, 1.5]:
            with self.assertRaises(ValueError):
                euler_totient(n)
