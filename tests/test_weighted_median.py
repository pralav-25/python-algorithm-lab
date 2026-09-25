import random
import unittest

from algorithm_lab.weighted_median import weighted_median


class Tests(unittest.TestCase):
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
