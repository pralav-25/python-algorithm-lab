"""Enumerate primitive positive Pythagorean triples with bounded hypotenuse.

limit is a nonnegative integer excluding bool; include c<=limit. Return a new
list of tuples (a,b,c), with a<b, gcd(a,b,c)=1, sorted by (c,a,b), resolving
equal hypotenuses by increasing legs. Euclid's formula takes O(limit) candidate
pairs, O(limit*log(limit+1)) gcd/sorting work, and O(limit) output storage.

>>> pythagorean_triples(20)
[(3, 4, 5), (5, 12, 13), (8, 15, 17)]
"""

from math import gcd, isqrt

from algorithm_lab._validation import integer


def pythagorean_triples(limit):
    integer(limit, "limit", minimum=0)
    result = []
    for m in range(2, isqrt(max(0, limit - 1)) + 1):
        for n in range(1, m):
            hypotenuse = m * m + n * n
            if hypotenuse > limit:
                break
            if (m - n) % 2 == 0 or gcd(m, n) != 1:
                continue
            a, b = sorted((m * m - n * n, 2 * m * n))
            result.append((a, b, hypotenuse))
    return sorted(result, key=lambda triple: (triple[2], triple[0], triple[1]))
