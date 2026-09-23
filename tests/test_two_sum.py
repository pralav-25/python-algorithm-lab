import random
import unittest

from algorithm_lab.two_sum import two_sum


class TwoSumTests(unittest.TestCase):
    def test_pair_order_against_nested_loop(self):
        rng = random.Random(3)
        for size in range(35):
            values = [rng.randrange(-8, 9) for _ in range(size)]
            for target in range(-10, 11):
                expected = next(
                    (
                        (i, j)
                        for j in range(size)
                        for i in range(j)
                        if values[i] + values[j] == target
                    ),
                    None,
                )
                self.assertEqual(two_sum(iter(values), target), expected)

    def test_no_reuse_and_large_integers(self):
        self.assertIsNone(two_sum([3], 6))
        self.assertEqual(two_sum([10**100, -(10**100)], 0), (0, 1))
