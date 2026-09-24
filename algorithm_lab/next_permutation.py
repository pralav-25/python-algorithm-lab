"""Return the next lexicographic arrangement, or None at the last arrangement.

Duplicates are supported. O(n) time and space for the returned list. The input
is copied and values need a total order. Empty/singleton inputs have no successor.

>>> next_permutation([1, 2, 1])
[2, 1, 1]
"""


def next_permutation(values):
    data = list(values)
    pivot = len(data) - 2
    while pivot >= 0 and not data[pivot] < data[pivot + 1]:
        pivot -= 1
    if pivot < 0:
        return None
    successor = len(data) - 1
    while not data[pivot] < data[successor]:
        successor -= 1
    data[pivot], data[successor] = data[successor], data[pivot]
    data[pivot + 1 :] = reversed(data[pivot + 1 :])
    return data
