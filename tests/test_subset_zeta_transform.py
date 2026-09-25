import random
import unittest

from algorithm_lab.subset_zeta_transform import subset_zeta_transform


class Tests(unittest.TestCase):
    def test_subset_enumeration(self):
        rng = random.Random(227)
        for bits in range(7):
            values = [rng.randrange(-10, 11) for _ in range(1 << bits)]
            expected = [
                sum(value for sub, value in enumerate(values) if sub & mask == sub)
                for mask in range(len(values))
            ]
            self.assertEqual(subset_zeta_transform(values), expected)

    def test_invalid(self):
        for values in [[], [1, 2, 3], [True], [1.5]]:
            with self.assertRaises(ValueError):
                subset_zeta_transform(values)
