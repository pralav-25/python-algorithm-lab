import math
import unittest

from algorithm_lab.legendre_exponent import legendre_exponent


class Tests(unittest.TestCase):
    def test_factorial_divisibility_oracle(self):
        for n in range(41):
            for prime in (2, 3, 5, 7, 11, 17, 47):
                remaining = math.factorial(n)
                expected = 0
                while remaining % prime == 0:
                    expected += 1
                    remaining //= prime
                self.assertEqual(legendre_exponent(n, prime), expected)

    def test_invalid(self):
        for args in ((-1, 2), (True, 2), (2.5, 2), (2, True), (2, 1), (2, 4), (2, 9), (2, 2.5)):
            with self.assertRaises(ValueError):
                legendre_exponent(*args)
