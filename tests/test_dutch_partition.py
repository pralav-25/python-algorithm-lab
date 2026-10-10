import itertools
import unittest

from algorithm_lab.dutch_partition import dutch_partition


class DutchPartitionTests(unittest.TestCase):
    def test_partition_and_permutation_invariants(self):
        for n in range(7):
            for data in itertools.product((-1, 0, 1), repeat=n):
                for pivot in range(-2, 3):
                    result = dutch_partition(iter(data), pivot)
                    self.assertCountEqual(result, data)
                    classes = [(value > pivot) - (value < pivot) for value in result]
                    self.assertEqual(classes, sorted(classes))

    def test_no_mutation_and_validation(self):
        data = [4, -3, 4, 1]
        original = data[:]
        self.assertCountEqual(dutch_partition(data, 4), data)
        self.assertEqual(data, original)
        for bad in [True, 1.2, "2"]:
            with self.assertRaises(ValueError):
                dutch_partition([bad], 0)
            with self.assertRaises(ValueError):
                dutch_partition([], bad)
