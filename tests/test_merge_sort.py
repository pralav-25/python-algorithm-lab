import random
import unittest

from algorithm_lab.merge_sort import merge_sort


class MergeSortTests(unittest.TestCase):
    def test_seeded_sort_oracle(self):
        rng = random.Random(5)
        for size in range(100):
            data = [rng.randrange(-10, 11) for _ in range(size)]
            before = data[:]
            self.assertEqual(merge_sort(data), sorted(data))
            self.assertEqual(data, before)

    def test_stability_and_key_calls(self):
        data = [("b", 1), ("a", 2), ("b", 3), ("a", 4)]
        calls = []

        def key(row):
            calls.append(row)
            return row[0]

        self.assertEqual(merge_sort(iter(data), key=key), sorted(data, key=lambda row: row[0]))
        self.assertEqual(calls, data)
