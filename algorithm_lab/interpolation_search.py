"""Find the first target occurrence by interpolating integer endpoints.

Values and target must be integers excluding bool. Ascending sortedness is an
unvalidated precondition. Returns -1 when absent and never modifies the input.
Integer validation costs O(n) time; the search itself is O(n) worst-case.
Auxiliary space is O(1). Arithmetic is exact, even for arbitrarily large ints.

>>> interpolation_search([1, 3, 3, 5, 9], 3)
1
>>> interpolation_search([4, 4, 4], 2)
-1
"""

from collections.abc import Sequence

from algorithm_lab._validation import integer


def interpolation_search(values: Sequence[int], target: int) -> int:
    integer(target, "target")
    for value in values:
        integer(value)
    left, right = 0, len(values) - 1
    found = -1
    while left <= right and values[left] <= target <= values[right]:
        if values[left] == values[right]:
            return left
        position = left + (target - values[left]) * (right - left) // (values[right] - values[left])
        if values[position] < target:
            left = position + 1
        else:
            if values[position] == target:
                found = position
            right = position - 1
    return found
