import itertools
import unittest

from algorithm_lab.palindrome_partition import palindrome_partition


class PartitionTests(unittest.TestCase):
    def test_all_cut_sets(self):
        for n in range(8):
            for chars in itertools.product("ab", repeat=n):
                text = "".join(chars)
                result = palindrome_partition(text)
                self.assertEqual("".join(result), text)
                self.assertTrue(all(piece and piece == piece[::-1] for piece in result))
                best = n
                for mask in range(1 << max(0, n - 1)):
                    cuts = [0] + [i for i in range(1, n) if mask & (1 << (i - 1))] + [n]
                    parts = [text[a:b] for a, b in zip(cuts, cuts[1:], strict=False) if a < b]
                    if all(p == p[::-1] for p in parts):
                        best = min(best, len(parts))
                self.assertEqual(len(result), best)
