import itertools
import random
import unittest

from algorithm_lab.insertion_sort import insertion_sort


class SortTests(unittest.TestCase):
    def test_exhaustive_small_inputs(self):
        for size in range(6):
            for values in itertools.product((-1, 0, 2), repeat=size):
                self.assertEqual(insertion_sort(values), sorted(values))

    def test_seeded_lists_and_no_mutation(self):
        rng = random.Random(213)
        for _ in range(80):
            values = [rng.randrange(-20, 21) for _ in range(rng.randrange(45))]
            original = values[:]
            self.assertEqual(insertion_sort(iter(values)), sorted(values))
            self.assertEqual(values, original)
        self.assertEqual(insertion_sort(["z", "a", "z"]), ["a", "z", "z"])

    def test_keys_evaluated_once_and_ties(self):
        data = [(2, "a"), (1, "b"), (2, "c"), (1, "d"), (2, "e")]
        calls = []

        def key(row):
            calls.append(row)
            return row[0]

        result = insertion_sort(data, key=key)
        self.assertEqual(calls, data)
        self.assertEqual([row[0] for row in result], [1, 1, 2, 2, 2])
        self.assertCountEqual(result, data)
        self.assertEqual(result, sorted(data, key=lambda row: row[0]))

    def test_non_orderable_payloads(self):
        rows = [dict(k=2), dict(k=1), dict(k=1)]
        self.assertEqual(
            [row["k"] for row in insertion_sort(rows, key=lambda row: row["k"])], [1, 1, 2]
        )
