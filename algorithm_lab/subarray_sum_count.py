"""Count contiguous target-sum slices using prefix frequencies.

Values and target are integers excluding bool. Return the number of nonempty
contiguous slices whose sum equals target. Negative values and repeated
prefix sums are supported. O(n) expected dictionary time and O(n) space.

>>> subarray_sum_count([0, 0, 0], 0)
6
"""

from algorithm_lab._validation import integer


def subarray_sum_count(values, target):
    integer(target, "target")
    frequencies, prefix, result = {0: 1}, 0, 0
    for value in values:
        integer(value)
        prefix += value
        result += frequencies.get(prefix - target, 0)
        frequencies[prefix] = frequencies.get(prefix, 0) + 1
    return result
