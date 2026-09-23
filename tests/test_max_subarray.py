import random
import unittest

from algorithm_lab.max_subarray import max_subarray


class MaxSubarrayTests(unittest.TestCase):
    def test_all_slices_oracle(self):
        rng = random.Random(6)
        for size in range(1, 25):
            values = [rng.randrange(-5, 6) for _ in range(size)]
            candidates = [
                (sum(values[i:j]), i, j) for i in range(size) for j in range(i + 1, size + 1)
            ]
            expected = min(candidates, key=lambda row: (-row[0], row[1], row[2]))
            self.assertEqual(max_subarray(values), expected)

    def test_negative_and_zero_ties(self):
        self.assertEqual(max_subarray([-4, -2, -2]), (-2, 1, 2))
        self.assertEqual(max_subarray([0, 0]), (0, 0, 1))
        self.assertEqual(max_subarray([0, 2]), (2, 0, 2))
        for values in [[], [True], [1.5]]:
            with self.assertRaises(ValueError):
                max_subarray(values)
