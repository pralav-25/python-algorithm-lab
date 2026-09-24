import random
import unittest

from algorithm_lab.rollback_disjoint_set import RollbackDisjointSet


class RollbackTests(unittest.TestCase):
    def test_nested_transactions(self):
        rng = random.Random(119)
        groups = RollbackDisjointSet(12)
        for _ in range(40):
            before = [[groups.find(a) == groups.find(b) for b in range(12)] for a in range(12)]
            count, token = groups.components, groups.snapshot()
            for _ in range(8):
                groups.union(rng.randrange(12), rng.randrange(12))
            middle = groups.snapshot()
            groups.union(0, 1)
            groups.rollback(middle)
            groups.rollback(token)
            self.assertEqual(groups.components, count)
            self.assertEqual(
                [[groups.find(a) == groups.find(b) for b in range(12)] for a in range(12)], before
            )
            groups.union(rng.randrange(12), rng.randrange(12))

    def test_noops_and_validation(self):
        groups = RollbackDisjointSet(2)
        self.assertFalse(groups.union(1, 1))
        self.assertEqual(groups.snapshot(), 0)
        for token in [-1, 1, True]:
            with self.assertRaises(ValueError):
                groups.rollback(token)
        for vertex in [-1, 2, False]:
            with self.assertRaises(ValueError):
                groups.find(vertex)
        with self.assertRaises(ValueError):
            RollbackDisjointSet(-1)
