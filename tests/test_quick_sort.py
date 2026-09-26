import itertools
import unittest

from algorithm_lab.quick_sort import quick_sort


class Tests(unittest.TestCase):
    def test_exhaustive_duplicate_arrays(self):
        for n in range(8):
            for values in itertools.product(range(3), repeat=n):
                self.assertEqual(quick_sort(iter(values)), sorted(values))

    def test_large_inputs_and_nonmutation(self):
        for values in [
            list(range(5000)),
            list(range(5000, 0, -1)),
            [7] * 10000,
            list("abracadabra"),
        ]:
            original = values[:]
            self.assertEqual(quick_sort(values), sorted(values))
            self.assertEqual(values, original)
