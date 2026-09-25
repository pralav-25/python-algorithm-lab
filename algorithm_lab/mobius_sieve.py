"""Linear sieve of the Mobius function.

Return mu(0)..mu(limit), using 0 as the unused mu(0) sentinel. The positive
values are 0 for square factors and (-1)^k for k distinct prime factors.
limit is a nonnegative integer excluding bool. O(limit) time and space.

>>> mobius_sieve(6)
[0, 1, -1, -1, 0, -1, 1]
"""

from algorithm_lab._validation import integer


def mobius_sieve(limit):
    integer(limit, minimum=0)
    mu, composite, primes = [0] * (limit + 1), [False] * (limit + 1), []
    if limit:
        mu[1] = 1
    for n in range(2, limit + 1):
        if not composite[n]:
            primes.append(n)
            mu[n] = -1
        for prime in primes:
            if n * prime > limit:
                break
            composite[n * prime] = True
            if n % prime == 0:
                break
            mu[n * prime] = -mu[n]
    return mu
