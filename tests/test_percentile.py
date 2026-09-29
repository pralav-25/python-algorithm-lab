import math
import statistics
import unittest

from algorithm_lab.percentile import percentile


class Tests(unittest.TestCase):
    def test_reflection_at_repeated_values_and_fractional_positions(self):
        values = [-30, -2, -2, 5, 19, 19, 47]
        original = values[:]
        for q in [0, 0.125, 0.25, 0.375, 0.5, 0.75, 1]:
            with self.subTest(q=q):
                self.assertAlmostEqual(
                    percentile(iter([-x for x in values]), q),
                    -percentile(values, 1 - q),
                )
                self.assertAlmostEqual(percentile(reversed(values), q), percentile(values, q))
        self.assertEqual(values, original)

    def test_reject_nonfinite_quantile_even_for_singleton(self):
        for q in [math.nan, math.inf, -math.inf]:
            with self.subTest(q=q), self.assertRaises(ValueError):
                percentile([3], q)

    def test_standard_library_quantiles(self):
        values = [9, -2, 7, 4, 4, 11, 1]
        expected = statistics.quantiles(values, n=100, method="inclusive")
        for i, value in enumerate(expected, 1):
            self.assertAlmostEqual(percentile(values, i / 100), value)
        self.assertEqual(percentile([3], 0.4), 3)
        self.assertEqual(percentile([-1e308, 1e308], 0.5), 0)
        self.assertEqual(percentile(values, 0), -2)
        self.assertEqual(percentile(values, 1), 11)

    def test_invalid(self):
        for values, q in [
            ([], 0.5),
            ([1], -0.1),
            ([1], 1.1),
            ([math.nan], 0.5),
            ([True], 0.5),
            ([1], True),
            ([10**1000], 0.5),
        ]:
            with self.assertRaises(ValueError):
                percentile(values, q)
