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

    def test_branching_history_against_explicit_partition_model(self):
        rng = random.Random(928)
        size = 9
        groups = RollbackDisjointSet(size)
        states = [[{v} for v in range(size)]]
        for _ in range(300):
            if rng.randrange(3):
                a, b = rng.randrange(size), rng.randrange(size)
                partition = states[-1]
                first = next(group for group in partition if a in group)
                second = next(group for group in partition if b in group)
                merged = first != second
                self.assertEqual(groups.union(a, b), merged)
                if merged:
                    states.append(
                        [group for group in partition if group != first and group != second]
                        + [first | second]
                    )
            else:
                token = rng.randrange(len(states))
                groups.rollback(token)
                states = states[: token + 1]
            self.assertEqual(groups.snapshot(), len(states) - 1)
            self.assertEqual(groups.components, len(states[-1]))
            for a in range(size):
                for b in range(size):
                    expected = any(a in group and b in group for group in states[-1])
                    self.assertEqual(groups.find(a) == groups.find(b), expected)

    def test_rejected_rollback_preserves_current_history(self):
        groups = RollbackDisjointSet(3)
        groups.union(0, 1)
        for token in (-1, 2, 0.0, True, None):
            with self.assertRaises(ValueError):
                groups.rollback(token)
            self.assertEqual(groups.snapshot(), 1)
            self.assertEqual(groups.components, 2)
            self.assertEqual(groups.find(0), groups.find(1))
        groups.rollback(0)
        self.assertEqual(groups.components, 3)
