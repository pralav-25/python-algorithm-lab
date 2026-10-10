import itertools
import unittest

from algorithm_lab.jump_search import jump_search


class JumpSearchTests(unittest.TestCase):
    def test_linear_oracle_and_duplicates(self):
        for size in range(8):
            for data in itertools.combinations_with_replacement(range(4), size):
                for target in range(-1, 5):
                    self.assertEqual(
                        jump_search(data, target), data.index(target) if target in data else -1
                    )

    def test_block_boundaries_and_no_mutation(self):
        data = [i // 7 for i in range(140)]
        original = data[:]
        for target in range(-1, 22):
            self.assertEqual(
                jump_search(data, target), data.index(target) if target in data else -1
            )
        self.assertEqual(data, original)
        self.assertEqual(jump_search(["a", "b", "b"], "b"), 1)
