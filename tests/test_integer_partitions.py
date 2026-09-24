import unittest

from algorithm_lab.integer_partitions import integer_partitions


class IntegerPartitionTests(unittest.TestCase):
    def test_coin_count_oracle(self):
        for total in range(16):
            counts = [1] + [0] * total
            for part in range(1, total + 1):
                for value in range(part, total + 1):
                    counts[value] += counts[value - part]
            partitions = list(integer_partitions(total))
            self.assertEqual(len(partitions), counts[total])
            self.assertEqual(len(partitions), len(set(partitions)))
            self.assertEqual(partitions, sorted(partitions, reverse=True))
            for partition in partitions:
                self.assertEqual(sum(partition), total)
                self.assertEqual(list(partition), sorted(partition, reverse=True))
                self.assertTrue(all(x > 0 for x in partition))

    def test_invalid(self):
        for total in [-1, True, 2.5]:
            with self.assertRaises(ValueError):
                integer_partitions(total)
