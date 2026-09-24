import random
import unittest

from algorithm_lab.sparse_table import SparseTable


class SparseTests(unittest.TestCase):
    def test_all_ranges(self):
        rng = random.Random(112)
        for n in range(1, 45):
            data = [rng.randrange(-20, 21) for _ in range(n)]
            table = SparseTable(iter(data))
            for a in range(n):
                for b in range(a + 1, n + 1):
                    self.assertEqual(table.query(a, b), min(data[a:b]))
        self.assertEqual(SparseTable(["z", "a"]).query(0, 2), "a")

    def test_invalid_ranges(self):
        for table, a, b in [
            (SparseTable([]), 0, 0),
            (SparseTable([2]), 0, 0),
            (SparseTable([2]), -1, 1),
            (SparseTable([2]), 0, 2),
            (SparseTable([2]), True, 1),
        ]:
            with self.assertRaises(ValueError):
                table.query(a, b)
