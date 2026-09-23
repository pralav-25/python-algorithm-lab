import math
import unittest

from algorithm_lab.prime_factorization import prime_factorization


class FactorizationTests(unittest.TestCase):
    def test_prime_factors_reconstruct_every_small_integer(self):
        for value in range(1, 2000):
            factors = prime_factorization(value)
            self.assertEqual(math.prod(p**power for p, power in factors.items()), value)
            self.assertEqual(list(factors), sorted(factors))
            for prime, power in factors.items():
                self.assertGreater(power, 0)
                self.assertGreaterEqual(prime, 2)
                self.assertTrue(all(prime % d for d in range(2, math.isqrt(prime) + 1)))

    def test_prime_powers_and_validation(self):
        self.assertEqual(prime_factorization(2**100), {2: 100})
        self.assertEqual(prime_factorization(99991), {99991: 1})
        for value in [0, -1, True, 2.0]:
            with self.assertRaises(ValueError):
                prime_factorization(value)
