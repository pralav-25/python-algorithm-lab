import itertools
import random
import unittest

from algorithm_lab.longest_increasing_subsequence import longest_increasing_subsequence as lis


class LISTests(unittest.TestCase):
    def test_exhaustive_subsequence_oracle(self):
        rng = random.Random(8)
        for size in range(11):
            values = [rng.randrange(6) for _ in range(size)]
            best = max(
                (
                    len(candidate)
                    for length in range(size + 1)
                    for candidate in itertools.combinations(values, length)
                    if all(a < b for a, b in itertools.pairwise(candidate))
                ),
                default=0,
            )
            result = lis(values)
            self.assertEqual(len(result), best)
            self.assertTrue(all(a < b for a, b in itertools.pairwise(result)))
            cursor = iter(values)
            self.assertTrue(all(any(value == item for item in cursor) for value in result))

    def test_duplicates_and_ordered_data(self):
        self.assertEqual(lis([2] * 100), [2])
        self.assertEqual(lis(list(range(100))), list(range(100)))
        self.assertEqual(lis([]), [])
