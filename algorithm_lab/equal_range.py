"""Return the half-open range of target values in sorted ascending data.

Both boundaries equal the insertion point when absent. O(log n) comparisons,
O(1) space. Values must have a total order; sortedness is a precondition.

>>> equal_range([1, 2, 2, 2, 4], 2)
(1, 4)
>>> equal_range([1, 4], 3)
(1, 1)
"""


def equal_range(values, target):
    left, right = 0, len(values)
    while left < right:
        middle = (left + right) // 2
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle
    start, right = left, len(values)
    while left < right:
        middle = (left + right) // 2
        if target < values[middle]:
            right = middle
        else:
            left = middle + 1
    return start, left
