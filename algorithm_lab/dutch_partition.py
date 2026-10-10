"""Return a three-way partition of integer values around pivot.

Accepts an iterable of signed integers and an integer pivot, excluding bool.
The new list contains values below pivot, then equal values, then values above
pivot. Order within groups is unspecified; all duplicates are retained. Input
is unchanged. Time: O(n); auxiliary space including the copy: O(n).

>>> dutch_partition([3, 2, 1, 2, 0], 2)
[0, 1, 2, 2, 3]
"""

from collections.abc import Iterable

from algorithm_lab._validation import integer


def dutch_partition(values: Iterable[int], pivot: int) -> list[int]:
    integer(pivot, "pivot")
    data = [integer(value) for value in values]
    low = current = 0
    high = len(data) - 1
    while current <= high:
        if data[current] < pivot:
            data[low], data[current] = data[current], data[low]
            low += 1
            current += 1
        elif data[current] > pivot:
            data[current], data[high] = data[high], data[current]
            high -= 1
        else:
            current += 1
    return data
