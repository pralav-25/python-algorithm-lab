import unittest

from algorithm_lab.bell_number import bell_number


def partitions(values):
    if not values:
        yield ()
        return
    first, *rest = values
    for blocks in partitions(rest):
        yield ((first,),) + blocks
        for index, block in enumerate(blocks):
            yield blocks[:index] + ((first,) + block,) + blocks[index + 1 :]


class Tests(unittest.TestCase):
    def test_set_partition_enumeration(self):
        for n in range(8):
            self.assertEqual(bell_number(n), sum(1 for _ in partitions(list(range(n)))))

    def test_invalid(self):
        for value in (-1, True, 2.5, "3", None):
            with self.assertRaises(ValueError):
                bell_number(value)
