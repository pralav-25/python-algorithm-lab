import random
import unittest

from algorithm_lab.radix_sort import radix_sort


class RadixSortTests(unittest.TestCase):
    def test_signed_and_large_integer_oracle(self):
        rng = random.Random(23)
        for size in range(70):
            data = [rng.randrange(-(2**140), 2**140) for _ in range(size)]
            before = data[:]
            self.assertEqual(radix_sort(data), sorted(data))
            self.assertEqual(data, before)

    def test_empty_equal_and_byte_boundaries(self):
        for data in [[], [0] * 10, [-9] * 10, [255, 256, 257, -256, -257, 0]]:
            self.assertEqual(radix_sort(iter(data)), sorted(data))

    def test_invalid_values(self):
        for data in [[True], [1.0], [None]]:
            with self.assertRaises(ValueError):
                radix_sort(data)
