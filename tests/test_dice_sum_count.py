import itertools
import unittest
from collections import Counter

from algorithm_lab.dice_sum_count import dice_sum_count


class Tests(unittest.TestCase):
    def test_enumerate_ordered_rolls(self):
        for dice in range(5):
            for faces in range(1, 5):
                histogram = Counter(
                    sum(outcome) for outcome in itertools.product(range(1, faces + 1), repeat=dice)
                )
                for total in range(dice * faces + 3):
                    self.assertEqual(dice_sum_count(dice, faces, total), histogram[total])
        self.assertEqual(dice_sum_count(0, 100, 0), 1)
        self.assertEqual(dice_sum_count(10, 1, 10), 1)

    def test_invalid(self):
        for args in [
            (-1, 6, 0),
            (True, 6, 0),
            (0, 0, 0),
            (0, False, 0),
            (0, 6, -1),
            (0, 6, True),
            (1.0, 6, 2),
            (1, 6.0, 2),
            (1, 6, 2.0),
        ]:
            with self.assertRaises(ValueError):
                dice_sum_count(*args)
