import random
import unittest

from algorithm_lab.disjoint_set import DisjointSet


class DisjointSetTests(unittest.TestCase):
    def test_set_partition_oracle(self):
        rng = random.Random(60)
        dsu, groups = DisjointSet(20), [{i} for i in range(20)]
        for _ in range(100):
            a, b = rng.randrange(20), rng.randrange(20)
            first = next(group for group in groups if a in group)
            second = next(group for group in groups if b in group)
            changed = first is not second
            self.assertEqual(dsu.union(a, b), changed)
            if changed:
                groups.remove(first)
                groups.remove(second)
                groups.append(first | second)
            self.assertEqual(set(dsu.groups()), set(map(frozenset, groups)))
            self.assertEqual(dsu.components, len(groups))
            self.assertTrue(dsu.connected(a, b))
            self.assertEqual(dsu.component_size(a), len(next(g for g in groups if a in g)))

    def test_empty_and_invalid_vertices(self):
        self.assertEqual(DisjointSet(0).groups(), [])
        dsu = DisjointSet(3)
        for vertex in [-1, 3, True, 1.5]:
            with self.assertRaises(ValueError):
                dsu.union(0, vertex)
        self.assertEqual(dsu.components, 3)
        for size in [-1, True, 1.2]:
            with self.assertRaises(ValueError):
                DisjointSet(size)
