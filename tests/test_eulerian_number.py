import itertools
import unittest

from algorithm_lab.eulerian_number import eulerian_number


class Tests(unittest.TestCase):
    def test_permutation_oracle(self):
        for n in range(8):
            counts = [0] * (n + 2)
            for order in itertools.permutations(range(n)):
                descents = sum(a > b for a, b in itertools.pairwise(order))
                counts[descents] += 1
            for k, expected in enumerate(counts):
                self.assertEqual(eulerian_number(n, k), expected)

    def test_invalid(self):
        for args in ((-1, 0), (0, -1), (True, 0), (1, True), (1.5, 0), (1, "0")):
            with self.assertRaises(ValueError):
                eulerian_number(*args)
