import math
import unittest

from algorithm_lab.entropy import entropy


class Tests(unittest.TestCase):
    def test_independent_product_entropy_is_additive(self):
        for left, right in [([1, 3], [2, 0, 5]), ([0, 7, 2], [1, 4, 9]), ([5], [1, 1])]:
            with self.subTest(left=left, right=right):
                joint = [a * b for a in left for b in right]
                self.assertAlmostEqual(entropy(iter(joint)), entropy(left) + entropy(right))
                self.assertAlmostEqual(entropy([0, *joint, 0]), entropy(joint))
                self.assertAlmostEqual(entropy(reversed(joint)), entropy(joint))

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
