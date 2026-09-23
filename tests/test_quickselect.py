import random
import unittest

from algorithm_lab.quickselect import quickselect


class QuickselectTests(unittest.TestCase):
    def test_all_ranks_against_sort(self):
        rng = random.Random(18)
        for size in range(1, 45):
            values = [rng.randrange(-8, 9) for _ in range(size)]
            before = values[:]
            self.assertEqual([quickselect(values, k) for k in range(size)], sorted(values))
            self.assertEqual(values, before)

    def test_equal_and_ordered(self):
        self.assertEqual(quickselect([4] * 100, 70), 4)
        self.assertEqual(quickselect(list(range(100, 0, -1)), 0), 1)

    def test_invalid_ranks(self):
        for data, rank in [([], 0), ([1], -1), ([1], 1), ([1], True), ([1], 0.5)]:
            with self.assertRaises(ValueError):
                quickselect(data, rank)
