import math
import unittest

from algorithm_lab.entropy import entropy


class Tests(unittest.TestCase):
    def test_known_distributions_and_scaling(self):
        for n in range(1, 30):
            self.assertAlmostEqual(entropy([1] * n), math.log2(n))
        self.assertEqual(entropy([0, 8, 0]), 0)
        self.assertAlmostEqual(entropy([1, 3]), 0.8112781244591328)
        self.assertAlmostEqual(entropy([1e308, 1e308]), 1)
        self.assertAlmostEqual(entropy([1, 3]), entropy([1e100, 3e100]))

    def test_invalid(self):
        for weights in [[], [0, 0], [-1, 2], [math.nan], [math.inf], [True], [10**1000]]:
            with self.assertRaises(ValueError):
                entropy(weights)
