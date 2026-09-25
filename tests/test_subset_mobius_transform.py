import random
import unittest

from algorithm_lab.subset_mobius_transform import subset_mobius_transform


class Tests(unittest.TestCase):
    def test_inclusion_exclusion_oracle(self):
        rng = random.Random(228)
        for bits in range(7):
            values = [rng.randrange(-10, 11) for _ in range(1 << bits)]
            expected = [
                sum(
                    (-1) ** (mask.bit_count() - sub.bit_count()) * value
                    for sub, value in enumerate(values)
                    if sub & mask == sub
                )
                for mask in range(len(values))
            ]
            self.assertEqual(subset_mobius_transform(values), expected)

    def test_invalid(self):
        for values in [[], [1, 2, 3], [True], [1.5]]:
            with self.assertRaises(ValueError):
                subset_mobius_transform(values)
