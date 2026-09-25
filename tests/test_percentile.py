import math
import statistics
import unittest

from algorithm_lab.percentile import percentile


class Tests(unittest.TestCase):
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
