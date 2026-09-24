import itertools
import unittest
from collections import Counter

from algorithm_lab.majority_element import majority_element


class MajorityTests(unittest.TestCase):
    def test_exhaustive_votes(self):
        for size in range(7):
            for data in itertools.product(range(3), repeat=size):
                candidates = [v for v, count in Counter(data).items() if count > size // 2]
                if candidates:
                    self.assertEqual(majority_element(data), candidates[0])
                else:
                    with self.assertRaises(ValueError):
                        majority_element(data)
        self.assertIsNone(majority_element([None, 1, None]))
        self.assertEqual(majority_element([[1], [2], [1]]), [1])
