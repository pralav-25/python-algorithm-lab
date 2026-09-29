import math
import random
import statistics
import unittest
from fractions import Fraction

from algorithm_lab.online_covariance import online_covariance


class Tests(unittest.TestCase):
    def test_affine_transforms_against_exact_covariance(self):
        pairs = [(-4, 8), (1, -3), (7, 2), (0, 6), (5, -9)]
        n = len(pairs)
        x_mean = Fraction(sum(x for x, _ in pairs), n)
        y_mean = Fraction(sum(y for _, y in pairs), n)
        moment = sum((x - x_mean) * (y - y_mean) for x, y in pairs)
        for sample in [False, True]:
            for scale_x, scale_y in [(3, -2), (0, 4), (-1, -7)]:
                transformed = [(scale_x * x + 1000, scale_y * y - 2000) for x, y in pairs]
                expected = float(scale_x * scale_y * moment / (n - int(sample)))
                with self.subTest(sample=sample, scale_x=scale_x, scale_y=scale_y):
                    self.assertAlmostEqual(
                        online_covariance(iter(transformed), sample=sample), expected
                    )
                    self.assertAlmostEqual(
                        online_covariance(reversed(transformed), sample=sample), expected
                    )

    def test_exact_covariance_at_large_offsets(self):
        # The centered observations are (-1, -1), (1, 1): sum products = 2.
        for offset in [1e16, -1e16]:
            values = [offset, offset + 2]
            pairs = list(zip(values, values, strict=True))
            self.assertEqual(online_covariance(iter(pairs), sample=True), 2)
            self.assertEqual(online_covariance(iter(pairs)), 1)
            reverse_pairs = zip(values, reversed(values), strict=True)
            self.assertEqual(online_covariance(reverse_pairs, sample=True), -2)

    def test_standard_library_oracle(self):
        rng = random.Random(256)
        for n in range(2, 60):
            x = [rng.uniform(-100, 100) for _ in range(n)]
            y = [rng.uniform(-100, 100) for _ in range(n)]
            expected = statistics.covariance(x, y)
            self.assertAlmostEqual(
                online_covariance(zip(x, y, strict=True), sample=True), expected, places=8
            )
            self.assertAlmostEqual(
                online_covariance(zip(x, y, strict=True)), expected * (n - 1) / n, places=8
            )
        self.assertEqual(online_covariance([(3, 5)]), 0)

    def test_invalid(self):
        for pairs in [[], [(True, 1)], [(math.nan, 1)], [(1e308, 1e308), (-1e308, -1e308)]]:
            with self.assertRaises(ValueError):
                online_covariance(pairs)
        with self.assertRaises(ValueError):
            online_covariance([(1, 2)], sample=True)
        with self.assertRaises(ValueError):
            online_covariance([(1, 2)], sample=1)
