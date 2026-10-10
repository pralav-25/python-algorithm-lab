import itertools
import unittest

from algorithm_lab.merge_sorted import merge_sorted


class MergeSortedTests(unittest.TestCase):
    def test_sorting_oracle(self):
        sequences = [
            values
            for n in range(5)
            for values in itertools.combinations_with_replacement(range(3), n)
        ]
        for first in sequences:
            for second in sequences:
                self.assertEqual(merge_sorted(iter(first), iter(second)), sorted(first + second))

    def test_stable_ties_key_calls_and_no_mutation(self):
        first = [(1, "a"), (2, "b"), (2, "c")]
        second = [(1, "d"), (2, "e"), (3, "f")]
        original = first[:], second[:]
        calls = []

        def key(row):
            calls.append(row)
            return row[0]

        self.assertEqual(
            merge_sorted(first, second, key=key), sorted(first + second, key=lambda row: row[0])
        )
        self.assertEqual(calls, first + second)
        self.assertEqual((first, second), original)
