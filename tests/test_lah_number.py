import itertools
import unittest

from algorithm_lab.lah_number import lah_number


class Tests(unittest.TestCase):
    def test_list_partition_enumeration(self):
        self.assertEqual(lah_number(0, 0), 1)
        for n in range(1, 6):
            for k in range(1, n + 1):
                partitions = set()
                for order in itertools.permutations(range(n)):
                    for cuts in itertools.combinations(range(1, n), k - 1):
                        boundaries = (0,) + cuts + (n,)
                        blocks = tuple(
                            order[left:right] for left, right in itertools.pairwise(boundaries)
                        )
                        partitions.add(tuple(sorted(blocks)))
                self.assertEqual(lah_number(n, k), len(partitions))

    def test_boundaries_and_invalid(self):
        for args in ((0, 1), (4, 0), (2, 3)):
            self.assertEqual(lah_number(*args), 0)
        for args in ((-1, 0), (1, -1), (True, 1), (1, False), (2.5, 1), (1, "2")):
            with self.assertRaises(ValueError):
                lah_number(*args)
