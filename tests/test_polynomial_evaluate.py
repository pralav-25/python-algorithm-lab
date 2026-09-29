import random
import unittest

from algorithm_lab.polynomial_evaluate import polynomial_evaluate


class Tests(unittest.TestCase):
    def test_large_integer_cancellation_and_nonmutation(self):
        base = 10**100 + 7
        coefficients = [-(base**3), 3 * base**2, -3 * base, 1, 0, 0]
        original = coefficients[:]
        # These coefficients represent (x - base)**3.
        for offset in [-2, -1, 0, 1, 2]:
            self.assertEqual(polynomial_evaluate(iter(coefficients), base + offset), offset**3)
        self.assertEqual(polynomial_evaluate(coefficients, base), 0)
        self.assertEqual(coefficients, original)

    def test_power_sum_oracle(self):
        rng = random.Random(211)
        for _ in range(100):
            values = [rng.randrange(-10, 11) for _ in range(rng.randrange(12))]
            for x in [-100, -1, 0, 1, 100]:
                self.assertEqual(
                    polynomial_evaluate(iter(values), x),
                    sum(c * x**i for i, c in enumerate(values)),
                )

    def test_invalid(self):
        for values, x in [([True], 1), ([1.5], 2), ([1], False)]:
            with self.assertRaises(ValueError):
                polynomial_evaluate(values, x)
