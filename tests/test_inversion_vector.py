import unittest
from itertools import product

from algorithm_lab.inversion_vector import inversion_vector


class Tests(unittest.TestCase):
    def test_pair_count_oracle(self):
        for n in range(7):
            for values in product([-1, 0, 1], repeat=n):
                expected = [
                    sum(other < value for other in values[i + 1 :])
                    for i, value in enumerate(values)
                ]
                self.assertEqual(inversion_vector(values), expected)

    def test_invalid(self):
        with self.assertRaises(ValueError):
            inversion_vector([True])
