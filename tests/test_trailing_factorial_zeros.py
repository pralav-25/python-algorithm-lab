import math
import unittest

from algorithm_lab.trailing_factorial_zeros import trailing_factorial_zeros


class Tests(unittest.TestCase):
    def test_factorial_divisibility_oracle(self):
        for n in range(41):
            for base in range(2, 50):
                remaining = math.factorial(n)
                expected = 0
                while remaining % base == 0:
                    expected += 1
                    remaining //= base
                self.assertEqual(trailing_factorial_zeros(n, base), expected)

    def test_default_and_invalid(self):
        self.assertEqual(trailing_factorial_zeros(100), 24)
        for args in ((-1,), (True,), (2.5,), (3, 1), (3, True), (3, 2.5)):
            with self.assertRaises(ValueError):
                trailing_factorial_zeros(*args)
