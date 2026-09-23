"""Algorithm R: sample up to k stream positions without replacement.

Time O(n), storage O(k). If the stream is shorter than k, return every item in
input order. Sample output is otherwise unordered; equal values at different
positions remain distinct candidates. k=0 does not consume the stream. Supply a
random.Random instance for reproducibility; the module-level RNG is not modified.

>>> import random
>>> reservoir_sample(range(3), 5, rng=random.Random(1))
[0, 1, 2]
"""

import random
from collections.abc import Iterable
from typing import TypeVar

T = TypeVar("T")


def reservoir_sample(items: Iterable[T], k: int, *, rng: random.Random | None = None) -> list[T]:
    if isinstance(k, bool) or not isinstance(k, int) or k < 0:
        raise ValueError("k must be a nonnegative integer")
    if k == 0:
        return []
    generator = rng if rng is not None else random.Random()
    result = []
    for index, item in enumerate(items):
        if index < k:
            result.append(item)
        else:
            slot = generator.randrange(index + 1)
            if slot < k:
                result[slot] = item
    return result
