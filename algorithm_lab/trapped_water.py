"""Water volume retained by nonnegative integer unit-width bars.

O(n) time and O(n) space for validated input; the two-pointer scan uses O(1)
extra state. Empty input retains zero. Booleans/non-integers are rejected.

>>> trapped_water([3, 0, 2, 0, 4])
7
"""

from algorithm_lab._validation import integer


def trapped_water(heights):
    data = [integer(h, "height", minimum=0) for h in heights]
    left, right = 0, len(data) - 1
    left_max = right_max = water = 0
    while left <= right:
        if left_max <= right_max:
            left_max = max(left_max, data[left])
            water += left_max - data[left]
            left += 1
        else:
            right_max = max(right_max, data[right])
            water += right_max - data[right]
            right -= 1
    return water
