import unittest
from collections import deque
from itertools import product

from algorithm_lab.minimum_jumps import minimum_jumps


class Tests(unittest.TestCase):
    def test_overshoot_and_stalled_breadth_layers(self):
        for values, expected in [
            ([10**100, 0, 0, 0], 1),
            ([2, 0, 2, 0, 1], 2),
            ([3, 2, 1, 0, 10**100], None),
            ([1, 4, 0, 0, 0, 0], 2),
            ([0, 10**100], None),
        ]:
            original = values[:]
            with self.subTest(values=values):
                self.assertEqual(minimum_jumps(iter(values)), expected)
                self.assertEqual(minimum_jumps(values), expected)
                self.assertEqual(values, original)

    def test_reachable_and_unreachable_tails_are_validated(self):
        for values in [[10**100, True], [0, -1], [0, 1.5]]:
            with self.assertRaises(ValueError):
                minimum_jumps(iter(values))

    def test_bfs_oracle(self):
        for n in range(7):
            for values in product(range(3), repeat=n):
                queue, seen, expected = deque([(0, 0)]), {0}, None
                if not values:
                    expected = 0
                while queue and values:
                    i, distance = queue.popleft()
                    if i == n - 1:
                        expected = distance
                        break
                    for j in range(i + 1, min(n, i + values[i] + 1)):
                        if j not in seen:
                            seen.add(j)
                            queue.append((j, distance + 1))
                self.assertEqual(minimum_jumps(values), expected)

    def test_invalid(self):
        for values in [[-1], [True], [1.5]]:
            with self.assertRaises(ValueError):
                minimum_jumps(values)
