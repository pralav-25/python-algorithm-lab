import math
import unittest

from algorithm_lab.prime_sieve import prime_sieve


class PrimeSieveTests(unittest.TestCase):
    def test_trial_division_oracle(self):
        for limit in range(150):
            expected = [
                n
                for n in range(2, limit + 1)
                if all(n % divisor for divisor in range(2, math.isqrt(n) + 1))
            ]
            self.assertEqual(prime_sieve(limit), expected)
        self.assertEqual(len(prime_sieve(10000)), 1229)

    def test_square_boundary_and_validation(self):
        self.assertNotIn(49, prime_sieve(49))
        self.assertEqual(prime_sieve(2), [2])
        for limit in [-1, True, 3.5]:
            with self.assertRaises(ValueError):
                prime_sieve(limit)
