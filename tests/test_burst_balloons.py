import itertools
import random
import unittest

from algorithm_lab.burst_balloons import burst_balloons


class Tests(unittest.TestCase):
    @staticmethod
    def permutation_oracle(values):
        best = 0
        for order in itertools.permutations(range(len(values))):
            alive = list(range(len(values)))
            score = 0
            for index in order:
                position = alive.index(index)
                left = values[alive[position - 1]] if position else 1
                right = values[alive[position + 1]] if position + 1 < len(alive) else 1
                score += left * values[index] * right
                alive.pop(position)
            best = max(best, score)
        return best

    def test_all_burst_orders(self):
        rng = random.Random(731)
        cases = [[], [0], [3, 1, 5, 8], [2, 2, 2], [0, 5, 0, 3]]
        cases += [[rng.randrange(5) for _ in range(size)] for size in range(6) for _ in range(6)]
        for values in cases:
            original = values[:]
            self.assertEqual(burst_balloons(iter(values)), self.permutation_oracle(values))
            self.assertEqual(values, original)

    def test_invalid(self):
        for values in [[True], [-1], [2.0], [1, "2"]]:
            with self.assertRaises(ValueError):
                burst_balloons(values)
