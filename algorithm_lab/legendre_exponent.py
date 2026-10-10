"""Return the exponent of a prime in n! using Legendre's formula.

n is a nonnegative integer, and prime is a prime integer >=2; bool is excluded.
Composite prime arguments raise ValueError. Return an integer, with no ties.
Primality checking and repeated division use O(sqrt(prime)+log_prime(n+1))
arithmetic steps and O(1) integers, excluding big-integer costs.

>>> legendre_exponent(10, 2)
8
"""

from math import isqrt

from algorithm_lab._validation import integer


def legendre_exponent(n, prime):
    integer(n, "n", minimum=0)
    integer(prime, "prime", minimum=2)
    if any(prime % divisor == 0 for divisor in range(2, isqrt(prime) + 1)):
        raise ValueError("prime must be prime")
    exponent = 0
    while n:
        n //= prime
        exponent += n
    return exponent
