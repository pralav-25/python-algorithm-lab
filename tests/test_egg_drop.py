import unittest
from functools import lru_cache

from algorithm_lab.egg_drop import egg_drop


class Tests(unittest.TestCase):
    def test_minimax_floor_choices(self):
        @lru_cache(None)
        def oracle(eggs, floors):
            if not floors:
                return 0
            if eggs == 1:
                return floors
            return min(
                1 + max(oracle(eggs - 1, floor - 1), oracle(eggs, floors - floor))
                for floor in range(1, floors + 1)
            )

        for eggs in range(1, 6):
            for floors in range(25):
                self.assertEqual(egg_drop(eggs, floors), oracle(eggs, floors))
        self.assertEqual(egg_drop(2, 100), 14)
        self.assertEqual(egg_drop(1000, 1), 1)
        self.assertEqual(egg_drop(1000, 1023), 10)

    def test_invalid_even_zero_floors(self):
        for eggs, floors in [(0, 0), (True, 0), (1.0, 0), (2, -1), (2, False), (2, 1.5)]:
            with self.assertRaises(ValueError):
                egg_drop(eggs, floors)
