import math
import random
import unittest

from algorithm_lab.chinese_remainder import chinese_remainder


class CRTTests(unittest.TestCase):
    def test_brute_force_residue_oracle(self):
        rng = random.Random(44)
        for _ in range(250):
            rows = [(rng.randrange(-10, 11), rng.randrange(1, 9)) for _ in range(3)]
            period = math.lcm(*(modulus for _, modulus in rows))
            solutions = [
                n
                for n in range(period)
                if all(n % modulus == remainder % modulus for remainder, modulus in rows)
            ]
            if solutions:
                self.assertEqual(chinese_remainder(iter(rows)), (solutions[0], period))
            else:
                with self.assertRaises(ValueError):
                    chinese_remainder(rows)

    def test_empty_redundant_and_invalid_systems(self):
        self.assertEqual(chinese_remainder([]), (0, 1))
        self.assertEqual(chinese_remainder([(9, 1)]), (0, 1))
        self.assertEqual(chinese_remainder([(2, 4), (2, 4)]), (2, 4))
        for rows in [[(0, 0)], [(1, -2)], [(True, 3)], [(1.2, 3)]]:
            with self.assertRaises(ValueError):
                chinese_remainder(rows)
