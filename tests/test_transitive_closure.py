import random
import unittest

from algorithm_lab.transitive_closure import transitive_closure


class ClosureTests(unittest.TestCase):
    def test_boolean_warshall_oracle(self):
        rng = random.Random(146)
        for n in range(9):
            for _ in range(30):
                graph = {a: [b for b in range(n) if rng.randrange(4) == 0] for a in range(n)}
                for reflexive in [False, True]:
                    matrix = [
                        [b in graph[a] or (reflexive and a == b) for b in range(n)]
                        for a in range(n)
                    ]
                    for k in range(n):
                        for a in range(n):
                            for b in range(n):
                                matrix[a][b] |= matrix[a][k] and matrix[k][b]
                    self.assertEqual(
                        transitive_closure(graph, reflexive=reflexive),
                        {a: frozenset(b for b in range(n) if matrix[a][b]) for a in range(n)},
                    )
        self.assertEqual(
            transitive_closure({None: ["x"]}, reflexive=False),
            {None: frozenset(["x"]), "x": frozenset()},
        )
