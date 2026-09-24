import unittest

from algorithm_lab.set_partitions import set_partitions


class SetPartitionTests(unittest.TestCase):
    def test_bell_numbers_and_canonical_structure(self):
        for size, bell in enumerate([1, 1, 2, 5, 15, 52, 203, 877]):
            result = list(set_partitions(size))
            self.assertEqual(len(result), bell)
            self.assertEqual(len(set(result)), bell)
            for partition in result:
                self.assertEqual(sorted(v for block in partition for v in block), list(range(size)))
                self.assertTrue(all(block and list(block) == sorted(block) for block in partition))
                self.assertEqual(
                    [block[0] for block in partition], sorted(block[0] for block in partition)
                )

    def test_invalid(self):
        for size in [-1, False, "3"]:
            with self.assertRaises(ValueError):
                set_partitions(size)
