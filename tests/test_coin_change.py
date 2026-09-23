import unittest
from collections import deque

from algorithm_lab.coin_change import coin_change


class CoinChangeTests(unittest.TestCase):
    def test_shortest_sum_graph_oracle(self):
        for coins in [[], [1], [2, 5], [1, 3, 4], [4, 6], [2, 2, 3]]:
            distances, queue = {0: 0}, deque([0])
            while queue:
                total = queue.popleft()
                for coin in coins:
                    if total + coin <= 40 and total + coin not in distances:
                        distances[total + coin] = distances[total] + 1
                        queue.append(total + coin)
            for amount in range(41):
                result = coin_change(coins, amount)
                if amount not in distances:
                    self.assertIsNone(result)
                else:
                    self.assertEqual(len(result), distances[amount])
                    self.assertEqual(sum(result), amount)
                    self.assertTrue(all(coin in coins for coin in result))

    def test_invalid_inputs(self):
        for coins, amount in [([0], 1), ([-1], 1), ([True], 2), ([1], -1), ([1], True)]:
            with self.assertRaises(ValueError):
                coin_change(coins, amount)
