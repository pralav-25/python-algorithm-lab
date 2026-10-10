import itertools
import unittest

from algorithm_lab.h_index import h_index


class HIndexTests(unittest.TestCase):
    def test_independent_threshold_oracle(self):
        for n in range(6):
            for values in itertools.product(range(4), repeat=n):
                expected = max(h for h in range(n + 1) if sum(value >= h for value in values) >= h)
                self.assertEqual(h_index(iter(values)), expected)

    def test_boundaries_and_validation(self):
        values = [10**100, 0, 10**100]
        self.assertEqual(h_index(values), 2)
        self.assertEqual(values, [10**100, 0, 10**100])
        for bad in [-1, True, 1.2, "2"]:
            with self.assertRaises(ValueError):
                h_index([bad])
