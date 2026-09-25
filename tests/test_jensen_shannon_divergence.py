import math
import unittest

from algorithm_lab.jensen_shannon_divergence import jensen_shannon_divergence


class Tests(unittest.TestCase):
    def test_known_values_and_symmetry(self):
        self.assertEqual(jensen_shannon_divergence([1, 0], [0, 1]), 1)
        self.assertEqual(jensen_shannon_divergence([1, 3], [2, 6]), 0)
        expected = 0.31127812445913283
        self.assertAlmostEqual(jensen_shannon_divergence([1, 0], [1, 1]), expected)
        for a, b in [([1, 2, 0], [2, 1, 4]), ([1e308, 0], [1e308, 1e308])]:
            self.assertAlmostEqual(jensen_shannon_divergence(a, b), jensen_shannon_divergence(b, a))
        self.assertTrue(math.isfinite(jensen_shannon_divergence([5e-324, 1], [0, 1])))

    def test_invalid(self):
        for a, b in [
            ([], []),
            ([1], [1, 2]),
            ([0], [1]),
            ([-1], [1]),
            ([math.nan], [1]),
            ([True], [1]),
        ]:
            with self.assertRaises(ValueError):
                jensen_shannon_divergence(a, b)
