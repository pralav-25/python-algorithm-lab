"""Find the smallest primitive root of an integer modulus.

modulus is an integer >=2 excluding bool. Return the smallest positive residue
generating all coprime residues, or None when no generator exists. Thus ties
choose the least residue. Trial division and an increasing candidate search use
O(sqrt(modulus)+modulus*log(modulus)**2) modular arithmetic steps, and
O(log(modulus)) integer storage; big-integer costs are additional.

>>> primitive_root(7)
3
>>> primitive_root(8) is None
True
"""

from math import gcd

from algorithm_lab._validation import integer


def primitive_root(modulus):
    integer(modulus, "modulus", minimum=2)
    remaining, totient, factor = modulus, modulus, 2
    while factor * factor <= remaining:
        if remaining % factor == 0:
            totient -= totient // factor
            while remaining % factor == 0:
                remaining //= factor
        factor += 1
    if remaining > 1:
        totient -= totient // remaining
    remaining, factor, prime_divisors = totient, 2, []
    while factor * factor <= remaining:
        if remaining % factor == 0:
            prime_divisors.append(factor)
            while remaining % factor == 0:
                remaining //= factor
        factor += 1
    if remaining > 1:
        prime_divisors.append(remaining)
    for candidate in range(1, modulus):
        if gcd(candidate, modulus) == 1 and all(
            pow(candidate, totient // prime, modulus) != 1 for prime in prime_divisors
        ):
            return candidate
    return None
