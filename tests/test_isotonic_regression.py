import unittest
from fractions import Fraction
from itertools import product

from algorithm_lab.isotonic_regression import isotonic_regression


class Tests(unittest.TestCase):
    def test_exact_rational_projection_conditions(self):
        for values in [
            [Fraction(7, 3), Fraction(-2, 5), Fraction(1, 7), Fraction(9, 2)],
            [Fraction(8, 9), Fraction(7, 9), Fraction(-5, 9), Fraction(-8, 9)],
            [Fraction(-4, 3), Fraction(-1, 3), Fraction(2, 3)],
        ]:
            original = values[:]
            fitted = isotonic_regression(iter(values))
            self.assertTrue(all(isinstance(v, Fraction) for v in fitted))
            self.assertEqual(fitted, sorted(fitted))
            self.assertEqual(isotonic_regression(fitted), fitted)
            residual = Fraction(0)
            for i, (observation, estimate) in enumerate(zip(values, fitted, strict=True)):
                residual += observation - estimate
                self.assertGreaterEqual(residual, 0)
                if i == len(fitted) - 1 or fitted[i] < fitted[i + 1]:
                    self.assertEqual(residual, 0)
            self.assertEqual(values, original)

    def test_all_contiguous_block_partitions(self):
        self.assertEqual(isotonic_regression([]), [])
        for n in range(1, 6):
            for values in product(range(3), repeat=n):
                costs = []
                for mask in range(1 << (n - 1)):
                    ends = [0] + [i for i in range(1, n) if mask >> (i - 1) & 1] + [n]
                    candidate = []
                    for a, b in zip(ends, ends[1:], strict=False):
                        candidate += [Fraction(sum(values[a:b]), b - a)] * (b - a)
                    if candidate == sorted(candidate):
                        costs.append(
                            sum((a - b) ** 2 for a, b in zip(values, candidate, strict=True))
                        )
                actual = isotonic_regression(values)
                self.assertEqual(actual, sorted(actual))
                self.assertEqual(
                    sum((a - b) ** 2 for a, b in zip(values, actual, strict=True)), min(costs)
                )

    def test_invalid(self):
        for values in [[True], [1.5]]:
            with self.assertRaises(ValueError):
                isotonic_regression(values)
