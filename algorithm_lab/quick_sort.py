"""Iterative three-way quicksort returning a new list of comparable values.

Equal values share one partition; the sort is not stable. The middle element is
the pivot. Expected O(n log n) time for randomly ordered input, worst-case O(n
squared), O(n) space including the returned list. Input iterables are not mutated.
Values must have a consistent total order; NaN is unsupported.

>>> quick_sort([3, 1, 3, 2])
[1, 2, 3, 3]
"""


def quick_sort(values):
    values = list(values)
    stack = [(0, len(values))]
    while stack:
        start, stop = stack.pop()
        if stop - start < 2:
            continue
        pivot = values[(start + stop) // 2]
        low, current, high = start, start, stop
        while current < high:
            if values[current] < pivot:
                values[low], values[current] = values[current], values[low]
                low += 1
                current += 1
            elif pivot < values[current]:
                high -= 1
                values[current], values[high] = values[high], values[current]
            else:
                current += 1
        stack.extend(((start, low), (high, stop)))
    return values
