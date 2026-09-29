import random
import unittest

from algorithm_lab.weighted_median import weighted_median


class Tests(unittest.TestCase):
    def test_huge_exact_weights_and_zero_mass_outliers(self):
        weight = 10**100
        values = [-(10**200), -7, 11, 10**200]
        original = values[:]
        self.assertEqual(weighted_median(iter(values), iter([0, weight, weight, 0])), -7)
        self.assertEqual(weighted_median(values, [0, weight, weight + 1, 0]), 11)
        self.assertEqual(values, original)

    def test_splitting_repeated_values_preserves_lower_median(self):
        self.assertEqual(weighted_median([9, -3, 5], [6, 3, 3]), 5)
        self.assertEqual(weighted_median([9, -3, 9, 5, -3], [2, 1, 4, 3, 2]), 5)

    def test_expanded_sample_oracle(self):
        rng = random.Random(251)
        for _ in range(100):
            values = [rng.randrange(-5, 6) for _ in range(10)]
            weights = [rng.randrange(4) for _ in values]
            expanded = sorted(v for v, w in zip(values, weights, strict=True) for _ in range(w))
            if expanded:
                actual = weighted_median(values, weights)
                self.assertEqual(actual, expanded[(len(expanded) - 1) // 2])
                cost = sum(w * abs(v - actual) for v, w in zip(values, weights, strict=True))
                self.assertEqual(
                    cost,
                    min(
                        sum(w * abs(v - c) for v, w in zip(values, weights, strict=True))
                        for c in values
                    ),
                )

    def test_invalid(self):
        for a, w in [([], []), ([1], []), ([1], [0]), ([1], [-1]), ([True], [1]), ([1], [True])]:
            with self.assertRaises(ValueError):
                weighted_median(a, w)
