"""Find primes in a half-open interval with segmented marking.

Integer bounds satisfy 0 <= start <= stop, excluding bool. Return primes
in ascending order, including start and excluding stop. With n = stop and
w = stop-start, storage is O(sqrt(n)+w); time is
O(sqrt(n) log log(n+2) + w log log(n+2)).

>>> segmented_sieve(10, 20)
[11, 13, 17, 19]
"""

from math import isqrt

from algorithm_lab._validation import integer


def segmented_sieve(start, stop):
    integer(start, "start", minimum=0)
    integer(stop, "stop", minimum=start)
    if stop <= 2 or start == stop:
        return []
    low = max(2, start)
    limit = isqrt(stop - 1)
    base = [True] * (limit + 1)
    segment = [True] * (stop - low)
    for prime in range(2, limit + 1):
        if base[prime]:
            for multiple in range(prime * prime, limit + 1, prime):
                base[multiple] = False
            first = max(prime * prime, ((low + prime - 1) // prime) * prime)
            for multiple in range(first, stop, prime):
                segment[multiple - low] = False
    return [low + offset for offset, prime in enumerate(segment) if prime]
