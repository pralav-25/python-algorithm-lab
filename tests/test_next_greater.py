import itertools
import unittest

from algorithm_lab.next_greater import next_greater


class NextGreaterTests(unittest.TestCase):
    def test_exhaustive(self):
        for n in range(7):
            for data in itertools.product(range(3), repeat=n):
                expected = [
                    next((j for j in range(i + 1, n) if data[j] > data[i]), -1) for i in range(n)
                ]
                self.assertEqual(next_greater(data), expected)
