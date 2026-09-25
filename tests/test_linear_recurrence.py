import random
import unittest

from algorithm_lab.linear_recurrence import linear_recurrence


class Tests(unittest.TestCase):
    def test_direct_recurrence_oracle(self):
        rng = random.Random(219)
        for k in range(1, 6):
            initial = [rng.randrange(-3, 4) for _ in range(k)]
            coefficients = [rng.randrange(-2, 3) for _ in range(k)]
            direct = initial[:]
            for n in range(k, 30):
                direct.append(sum(c * direct[n - j - 1] for j, c in enumerate(coefficients)))
            for n, expected in enumerate(direct):
                self.assertEqual(linear_recurrence(initial, coefficients, n), expected)

    def test_invalid(self):
        for a, c, n in [([], [], 0), ([1], [1, 2], 0), ([True], [1], 0), ([1], [1], -1)]:
            with self.assertRaises(ValueError):
                linear_recurrence(a, c, n)
