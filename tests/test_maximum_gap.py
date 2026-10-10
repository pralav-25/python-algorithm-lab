import itertools
import random
import unittest

from algorithm_lab.maximum_gap import maximum_gap


class MaximumGapTests(unittest.TestCase):
    def test_sorting_oracle(self):
        for n in range(6):
            for values in itertools.product((-3, 0, 2), repeat=n):
                ordered = sorted(values)
                expected = max(
                    (b - a for a, b in zip(ordered, ordered[1:], strict=False)), default=0
                )
                self.assertEqual(maximum_gap(iter(values)), expected)
        rng = random.Random(61)
        for _ in range(100):
            data = [rng.randrange(-10000, 10001) for _ in range(rng.randrange(30))]
            original = data[:]
            ordered = sorted(data)
            self.assertEqual(
                maximum_gap(data),
                max((b - a for a, b in zip(ordered, ordered[1:], strict=False)), default=0),
            )
            self.assertEqual(data, original)

    def test_huge_range_and_validation(self):
        self.assertEqual(maximum_gap([-(10**100), 10**100]), 2 * 10**100)
        for bad in [True, 1.2, "2"]:
            with self.assertRaises(ValueError):
                maximum_gap([bad])
