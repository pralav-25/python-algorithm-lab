import itertools
import unittest

from algorithm_lab.exponential_search import exponential_search


class ExponentialSearchTests(unittest.TestCase):
    def test_first_match_against_linear_oracle(self):
        for size in range(7):
            for data in itertools.combinations_with_replacement(range(4), size):
                for target in range(-1, 5):
                    expected = data.index(target) if target in data else -1
                    self.assertEqual(exponential_search(data, target), expected)

    def test_power_of_two_boundaries_and_no_mutation(self):
        data = list(range(257))
        original = data[:]
        for target in [0, 1, 2, 3, 4, 7, 8, 127, 128, 255, 256, 300]:
            self.assertEqual(exponential_search(data, target), target if target < len(data) else -1)
        self.assertEqual(data, original)
        self.assertEqual(exponential_search(["a", "b", "b"], "b"), 1)
