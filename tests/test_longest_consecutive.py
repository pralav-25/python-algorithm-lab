import itertools
import unittest

from algorithm_lab.longest_consecutive import longest_consecutive


class LongestConsecutiveTests(unittest.TestCase):
    def test_sorted_unique_oracle(self):
        for n in range(6):
            for values in itertools.product((-2, -1, 1, 2), repeat=n):
                ordered = sorted(set(values))
                longest = run = 0
                previous = None
                for value in ordered:
                    run = run + 1 if previous is not None and value == previous + 1 else 1
                    longest = max(longest, run)
                    previous = value
                self.assertEqual(longest_consecutive(iter(values)), longest)

    def test_input_and_validation(self):
        values = [10**100, 10**100 + 1, 10**100 - 1]
        original = values[:]
        self.assertEqual(longest_consecutive(values), 3)
        self.assertEqual(values, original)
        for bad in [True, 1.2, "2"]:
            with self.assertRaises(ValueError):
                longest_consecutive([bad])
