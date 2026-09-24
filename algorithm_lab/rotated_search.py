"""Find a target in a rotation of a strictly increasing sequence; absent gives -1.

O(log n) time and O(1) space. Distinctness and rotation-of-sorted order are
preconditions and are not scanned. Values must have a total order.

>>> rotated_search([5, 8, 1, 2, 3], 2)
3
"""


def rotated_search(values, target):
    left, right = 0, len(values) - 1
    while left <= right:
        middle = (left + right) // 2
        if values[middle] == target:
            return middle
        if values[left] <= values[middle]:
            if values[left] <= target < values[middle]:
                right = middle - 1
            else:
                left = middle + 1
        elif values[middle] < target <= values[right]:
            left = middle + 1
        else:
            right = middle - 1
    return -1
