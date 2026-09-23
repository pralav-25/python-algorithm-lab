import random
import unittest

from algorithm_lab.heap_sort import heap_sort


class HeapSortTests(unittest.TestCase):
    def test_against_builtin_sort(self):
        rng = random.Random(99)
        for size in range(120):
            data = [rng.randrange(-30, 31) for _ in range(size)]
            before = data[:]
            self.assertEqual(heap_sort(data), sorted(data))
            self.assertEqual(data, before)

    def test_ordered_and_string_values(self):
        for data in [[], [1], list(range(100)), list(range(100, 0, -1)), list("banana")]:
            self.assertEqual(heap_sort(iter(data)), sorted(data))
