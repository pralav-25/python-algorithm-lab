import itertools
import unittest

from algorithm_lab.histogram_area import histogram_area


class HistogramTests(unittest.TestCase):
    def test_all_small_histograms(self):
        for n in range(7):
            for heights in itertools.product(range(3), repeat=n):
                expected = max(
                    (min(heights[a:b]) * (b - a) for a in range(n) for b in range(a + 1, n + 1)),
                    default=0,
                )
                self.assertEqual(histogram_area(heights), expected)

    def test_invalid(self):
        for heights in [[-1], [True], [1.5]]:
            with self.assertRaises(ValueError):
                histogram_area(heights)
