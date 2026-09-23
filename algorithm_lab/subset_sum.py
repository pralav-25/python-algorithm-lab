"""Return whether some subset sums to target, using each input element at most once.

Values and target must be nonnegative integers, excluding booleans. The empty
subset reaches zero. Values above target are skipped before shifting. Storage is
O(target) bits; work is O(n * target) bit operations (word-parallel in Python).

>>> subset_sum([3, 7, 11], 10)
True
>>> subset_sum([3], 6)
False
"""


def subset_sum(values, target: int) -> bool:
    if isinstance(target, bool) or not isinstance(target, int) or target < 0:
        raise ValueError("target must be a nonnegative integer")
    reachable = 1
    mask = (1 << (target + 1)) - 1
    for value in values:
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError("values must be nonnegative integers")
        if value <= target:
            reachable = (reachable | (reachable << value)) & mask
    return bool(reachable & (1 << target))
