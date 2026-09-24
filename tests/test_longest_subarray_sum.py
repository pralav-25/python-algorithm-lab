import random
import unittest

from algorithm_lab.longest_subarray_sum import longest_subarray_sum


class SubarrayTests(unittest.TestCase):
    def test_brute_force(self):
        rng = random.Random(125)
        for _ in range(400):
            data = [rng.randrange(-3, 4) for _ in range(rng.randrange(15))]
            target = rng.randrange(-6, 7)
            candidates = [
                (a, b)
                for a in range(len(data))
                for b in range(a + 1, len(data) + 1)
                if sum(data[a:b]) == target
            ]
            expected = min(candidates, key=lambda p: (p[0] - p[1], p[0]), default=None)
            self.assertEqual(longest_subarray_sum(iter(data), target), expected)

    def test_invalid(self):
        for values, target in [([True], 1), ([1.2], 1), ([], False)]:
            with self.assertRaises(ValueError):
                longest_subarray_sum(values, target)
