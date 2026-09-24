import random
import unittest

from algorithm_lab.find_directed_cycle import find_directed_cycle


class CycleTests(unittest.TestCase):
    def test_kahn_oracle_and_witnesses(self):
        rng = random.Random(148)
        for _ in range(300):
            n = rng.randrange(10)
            graph = {a: [b for b in range(n) if rng.randrange(5) == 0] for a in range(n)}
            incoming = [sum(b in rows for rows in graph.values()) for b in range(n)]
            queue = [i for i in range(n) if not incoming[i]]
            removed = 0
            while queue:
                node = queue.pop()
                removed += 1
                for neighbor in graph[node]:
                    incoming[neighbor] -= 1
                    if not incoming[neighbor]:
                        queue.append(neighbor)
            cycle = find_directed_cycle(graph)
            self.assertEqual(bool(cycle), removed < n)
            if cycle:
                self.assertEqual(cycle[0], cycle[-1])
                self.assertEqual(len(set(cycle[:-1])), len(cycle) - 1)
                self.assertTrue(all(b in graph[a] for a, b in zip(cycle, cycle[1:], strict=False)))
        self.assertEqual(find_directed_cycle({None: [None]}), [None, None])
        self.assertEqual(find_directed_cycle({i: [i + 1] for i in range(5000)}), [])
