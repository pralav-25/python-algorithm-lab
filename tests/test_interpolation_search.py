import itertools
import random
import unittest

from algorithm_lab.interpolation_search import interpolation_search


class InterpolationSearchTests(unittest.TestCase):
    def test_linear_oracle(self):
        for size in range(7):
            for data in itertools.combinations_with_replacement(range(-2, 3), size):
                for target in range(-3, 4):
                    self.assertEqual(
                        interpolation_search(data, target),
                        data.index(target) if target in data else -1,
                    )

    def test_skewed_and_huge_integer_inputs(self):
        rng = random.Random(5)
        for _ in range(60):
            data = sorted(rng.randrange(-100, 101) ** 3 for _ in range(20))
            original = data[:]
            for target in data + [10**40]:
                self.assertEqual(
                    interpolation_search(data, target), data.index(target) if target in data else -1
                )
            self.assertEqual(data, original)
        self.assertEqual(interpolation_search([-(10**100), 0, 10**100], 0), 1)

    def test_validation(self):
        for bad in [True, 1.0, "1"]:
            with self.assertRaises(ValueError):
                interpolation_search([0, bad], 0)
            with self.assertRaises(ValueError):
                interpolation_search([], bad)
