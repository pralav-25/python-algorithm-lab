"""Return unique sorted 3-tuples summing to target, in lexicographic order.

Accepts an iterable of signed integers and an integer target, excluding bool.
Each tuple uses 3 distinct input positions; repeated values are permitted.
The input is not modified. Time: O(n²); auxiliary space: O(n), plus output.

>>> three_sum([-1, 0, 1, 2, -1, -4])
[(-1, -1, 2), (-1, 0, 1)]
"""

from collections.abc import Iterable

from algorithm_lab._validation import integer


def three_sum(values: Iterable[int], target: int = 0) -> list[tuple[int, ...]]:
    integer(target, "target")
    data = sorted(integer(value) for value in values)
    result = []

    for i in range(len(data) - 2):
        if i and data[i] == data[i - 1]:
            continue
        left, right = i + 1, len(data) - 1
        while left < right:
            total = data[i] + data[left] + data[right]
            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                result.append((data[i], data[left], data[right]))
                left += 1
                right -= 1
                while left < right and data[left] == data[left - 1]:
                    left += 1
                while left < right and data[right] == data[right + 1]:
                    right -= 1

    return result
