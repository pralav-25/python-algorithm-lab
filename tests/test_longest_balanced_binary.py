import itertools
import unittest

from algorithm_lab.longest_balanced_binary import longest_balanced_binary


class BalancedBinaryTests(unittest.TestCase):
    def test_brute_force_intervals_and_ties(self):
        for n in range(10):
            for data in itertools.product((0, 1), repeat=n):
                candidates = [(0, 0)] + [
                    (i, j)
                    for i in range(n)
                    for j in range(i + 1, n + 1)
                    if sum(data[i:j]) * 2 == j - i
                ]
                expected = min(candidates, key=lambda span: (span[0] - span[1], span[0]))
                self.assertEqual(longest_balanced_binary(iter(data)), expected)

    def test_no_mutation_and_validation(self):
        data = [1, 0, 0, 1]
        self.assertEqual(longest_balanced_binary(data), (0, 4))
        self.assertEqual(data, [1, 0, 0, 1])
        for bad in [-1, 2, True, 0.0, "0"]:
            with self.assertRaises(ValueError):
                longest_balanced_binary([bad])
