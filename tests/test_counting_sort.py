import random
import unittest

from algorithm_lab.counting_sort import counting_sort


class CountingSortTests(unittest.TestCase):
    def test_signed_values_and_iterators(self):
        rng = random.Random(4)
        for size in range(100):
            data = [rng.randrange(-30, 31) for _ in range(size)]
            self.assertEqual(counting_sort(iter(data)), sorted(data))
        self.assertEqual(counting_sort([10**100] * 3), [10**100] * 3)

    def test_range_limit(self):
        self.assertEqual(counting_sort([-1, 1], max_range=3), [-1, 1])
        with self.assertRaises(ValueError):
            counting_sort([-1, 1], max_range=2)

    def test_invalid_inputs(self):
        for data in [[True], [1.5], ["1"]]:
            with self.assertRaises(ValueError):
                counting_sort(data)
        for limit in [0, -1, True, 2.5]:
            with self.assertRaises(ValueError):
                counting_sort([], max_range=limit)
