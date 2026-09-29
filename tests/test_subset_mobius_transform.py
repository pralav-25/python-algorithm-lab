import random
import unittest

from algorithm_lab.subset_mobius_transform import subset_mobius_transform


class Tests(unittest.TestCase):
    def test_basis_inverse_has_alternating_superset_signs(self):
        for source in [0, 1, 128, 129, 255]:
            values = [0] * 256
            values[source] = 10**100 + 1
            original = values[:]
            expected = [
                (-1) ** (mask.bit_count() - source.bit_count()) * values[source]
                if mask & source == source
                else 0
                for mask in range(256)
            ]
            result = subset_mobius_transform(iter(values))
            self.assertEqual(result, expected)
            self.assertEqual(subset_mobius_transform(values), expected)
            result[source] = 0
            self.assertEqual(values, original)

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
