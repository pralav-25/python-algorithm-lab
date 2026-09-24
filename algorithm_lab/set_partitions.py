"""Yield all partitions of range(size) as tuples of nonempty ascending blocks.

Blocks are ordered by first member, so each unlabeled partition appears once.
Zero yields (). Enumeration costs O(n*Bell(n)) time and O(n) working space.
Recursion depth is n; use small sizes because the output grows very quickly.

>>> list(set_partitions(3))
[((0, 1, 2),), ((0, 1), (2,)), ((0, 2), (1,)), ((0,), (1, 2)), ((0,), (1,), (2,))]
"""

from algorithm_lab._validation import integer


def set_partitions(size):
    integer(size, "size", minimum=0)
    blocks = []

    def generate(value):
        if value == size:
            yield tuple(tuple(block) for block in blocks)
            return
        for i in range(len(blocks)):
            blocks[i].append(value)
            yield from generate(value + 1)
            blocks[i].pop()
        blocks.append([value])
        yield from generate(value + 1)
        blocks.pop()

    return generate(0)
