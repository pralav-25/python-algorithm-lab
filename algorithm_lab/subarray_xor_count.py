"""Count nonempty contiguous subarrays whose XOR equals target.

Accepts an iterable of nonnegative integers and a nonnegative integer target,
excluding bool. Repeated values and overlapping subarrays count separately.
Empty input gives zero and the input is not changed. Expected time and
auxiliary space: O(n), using prefix-XOR frequencies.

>>> subarray_xor_count([4, 2, 2, 6, 4], 6)
4
>>> subarray_xor_count([0, 0], 0)
3
"""

from collections.abc import Iterable

from algorithm_lab._validation import integer


def subarray_xor_count(values: Iterable[int], target: int) -> int:
    integer(target, "target", minimum=0)
    frequencies = {0: 1}
    prefix = answer = 0
    for value in values:
        prefix ^= integer(value, minimum=0)
        answer += frequencies.get(prefix ^ target, 0)
        frequencies[prefix] = frequencies.get(prefix, 0) + 1
    return answer
