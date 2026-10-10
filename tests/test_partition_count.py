import unittest

from algorithm_lab.partition_count import partition_count


def partitions(remaining, minimum=1):
    if remaining == 0:
        yield ()
    for first in range(minimum, remaining + 1):
        for rest in partitions(remaining - first, first):
            yield (first,) + rest


class Tests(unittest.TestCase):
    def test_unordered_enumeration(self):
        for n in range(18):
            self.assertEqual(partition_count(n), sum(1 for _ in partitions(n)))

    def test_invalid(self):
        for n in (-1, True, 1.5, "3", None):
            with self.assertRaises(ValueError):
                partition_count(n)
