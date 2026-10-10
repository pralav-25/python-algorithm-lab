import itertools
import unittest

from algorithm_lab.smallest_missing_positive import smallest_missing_positive


class MissingPositiveTests(unittest.TestCase):
    def test_membership_oracle(self):
        for n in range(6):
            for values in itertools.product((-1, 0, 1, 2, 3), repeat=n):
                expected = next(value for value in range(1, n + 2) if value not in values)
                self.assertEqual(smallest_missing_positive(iter(values)), expected)

    def test_boundary_and_validation(self):
        values = [4, 3, 2, 1, 1, 10**100]
        original = values[:]
        self.assertEqual(smallest_missing_positive(values), 5)
        self.assertEqual(values, original)
        for bad in [True, 1.2, "2"]:
            with self.assertRaises(ValueError):
                smallest_missing_positive([bad])
