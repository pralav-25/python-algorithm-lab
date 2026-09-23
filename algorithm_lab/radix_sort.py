"""Sort signed Python integers with least-significant-byte radix passes.

Subtracting the minimum maps negatives into nonnegative keys. Time is
O(d * (n + 256)), space O(n + 256), where d is the byte width of the value range.
The input is not changed; booleans and non-integer values raise ValueError.

>>> radix_sort([1000, -5, 0, -1000, 5])
[-1000, -5, 0, 5, 1000]
"""

from collections.abc import Iterable


def radix_sort(values: Iterable[int]) -> list[int]:
    data = list(values)
    if any(isinstance(value, bool) or not isinstance(value, int) for value in data):
        raise ValueError("values must be integers")
    if not data:
        return []
    offset = min(data)
    data = [value - offset for value in data]
    shift = 0
    remaining = max(data)
    while remaining:
        buckets = [[] for _ in range(256)]
        for value in data:
            buckets[(value >> shift) & 255].append(value)
        data = [value for bucket in buckets for value in bucket]
        shift += 8
        remaining >>= 8
    return [value + offset for value in data]
