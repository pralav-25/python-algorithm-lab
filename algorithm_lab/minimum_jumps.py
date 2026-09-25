"""Fewest forward jumps to the final array position.

Each entry is a nonnegative integer maximum jump length, excluding bool.
Return the minimum number of jumps from index 0 to the last index, or None
if unreachable. Empty and one-element inputs require 0 jumps. Greedy breadth
layers take O(n) time and O(n) copied input storage.

>>> minimum_jumps([2, 3, 1, 1, 4])
2
"""

from algorithm_lab._validation import integer


def minimum_jumps(lengths):
    lengths = list(lengths)
    for length in lengths:
        integer(length, "jump length", minimum=0)
    end, farthest, jumps = 0, 0, 0
    for i in range(len(lengths) - 1):
        farthest = max(farthest, i + lengths[i])
        if i == end:
            if farthest == end:
                return None
            jumps += 1
            end = farthest
            if end >= len(lengths) - 1:
                return jumps
    return jumps
