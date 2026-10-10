import itertools
import unittest
from collections import deque

from algorithm_lab.minimum_swaps_sort import minimum_swaps_sort


class MinimumSwapsTests(unittest.TestCase):
    def test_breadth_first_shortest_swap_oracle(self):
        for n in range(6):
            target = tuple(range(n))
            distances = {target: 0}
            queue = deque([target])
            while queue:
                state = queue.popleft()
                for i, j in itertools.combinations(range(n), 2):
                    successor = list(state)
                    successor[i], successor[j] = successor[j], successor[i]
                    successor = tuple(successor)
                    if successor not in distances:
                        distances[successor] = distances[state] + 1
                        queue.append(successor)
            for state, expected in distances.items():
                self.assertEqual(minimum_swaps_sort(state), expected)

    def test_signed_values_no_mutation_and_validation(self):
        values = [9, -3, 2, -10]
        original = values[:]
        self.assertEqual(minimum_swaps_sort(iter(values)), 1)
        self.assertEqual(values, original)
        for values in [[1, 1], [True], [1.2], ["2"]]:
            with self.assertRaises(ValueError):
                minimum_swaps_sort(values)
