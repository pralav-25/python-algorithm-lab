import random
import unittest

from algorithm_lab.binary_search import binary_search


class BinarySearchTests(unittest.TestCase):
    def test_boundaries(self):
        for values, target, expected in [
            ([], 1, -1),
            ([2], 2, 0),
            ([2], 1, -1),
            ([1, 2, 2, 9], 2, 1),
            ([1, 2, 9], 9, 2),
        ]:
            self.assertEqual(binary_search(values, target), expected)

    def test_seeded_linear_oracle(self):
        rng = random.Random(42)
        for _ in range(200):
            values = sorted(rng.randrange(-20, 21) for _ in range(rng.randrange(70)))
            before = values[:]
            for target in range(-22, 23):
                expected = values.index(target) if target in values else -1
                self.assertEqual(binary_search(values, target), expected)
            self.assertEqual(values, before)

    def test_strings(self):
        self.assertEqual(binary_search(("a", "b", "b", "z"), "b"), 1)
