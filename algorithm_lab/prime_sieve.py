"""Return all primes <= limit using O(limit log log limit) time and O(limit) space.

limit must be a nonnegative integer, excluding booleans. Limits below two return
an empty list. Composite marking begins at each prime's square.

>>> prime_sieve(20)
[2, 3, 5, 7, 11, 13, 17, 19]
"""

import math


def prime_sieve(limit: int) -> list[int]:
    if isinstance(limit, bool) or not isinstance(limit, int) or limit < 0:
        raise ValueError("limit must be a nonnegative integer")
    if limit < 2:
        return []
    flags = bytearray([1]) * (limit + 1)
    flags[0] = flags[1] = 0
    for prime in range(2, math.isqrt(limit) + 1):
        if flags[prime]:
            start = prime * prime
            flags[start::prime] = bytearray((limit - start) // prime + 1)
    return [value for value, prime in enumerate(flags) if prime]
