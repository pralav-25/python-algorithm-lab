"""Survivor among 0..size-1 when every step-th person is removed.

Counting starts at person zero as one; after removal it resumes at the next
person. size and step must be positive integers. O(size) time, O(1) integer slots.

>>> josephus(7, 3)
3
"""

from algorithm_lab._validation import integer


def josephus(size, step):
    integer(size, "size", minimum=1)
    integer(step, "step", minimum=1)
    survivor = 0
    for count in range(2, size + 1):
        survivor = (survivor + step) % count
    return survivor
