import itertools
import unittest

from algorithm_lab.kth_two_sorted import kth_two_sorted


class KthTwoSortedTests(unittest.TestCase):
    def test_all_ranks_against_sorted_concatenation(self):
        sequences = [
            values
            for n in range(5)
            for values in itertools.combinations_with_replacement(range(3), n)
        ]
        for a in sequences:
            for b in sequences:
                for k, expected in enumerate(sorted(a + b)):
                    self.assertEqual(kth_two_sorted(a, b, k), expected)

    def test_unbalanced_inputs_and_no_mutation(self):
        a, b = [1], list(range(100))
        for k, expected in enumerate(sorted(a + b)):
            self.assertEqual(kth_two_sorted(a, b, k), expected)
            self.assertEqual(kth_two_sorted(b, a, k), expected)
        self.assertEqual(a, [1])
        self.assertEqual(b, list(range(100)))
        self.assertEqual(kth_two_sorted(["a"], ["b"], 1), "b")

    def test_invalid_rank(self):
        for k in [-1, 2, True, 0.5, "0"]:
            with self.assertRaises(ValueError):
                kth_two_sorted([1], [2], k)
        with self.assertRaises(ValueError):
            kth_two_sorted([], [], 0)
