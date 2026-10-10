"""Return the exponent of the multiplicative group modulo n.

n is a positive integer excluding bool. Return the least positive k such that
a**k == 1 modulo n for every a coprime to n, using lambda(1)=1. There are no
ties. Trial factorization and prime-power formulas take O(sqrt(n)) arithmetic
steps and O(1) integers of storage, excluding big-integer and gcd costs.

>>> carmichael_function(8)
2
>>> carmichael_function(45)
12
"""

from math import lcm

from algorithm_lab._validation import integer


def carmichael_function(n):
    integer(n, "n", minimum=1)
    remaining, factor, result = n, 2, 1
    while factor * factor <= remaining:
        exponent, power = 0, 1
        while remaining % factor == 0:
            remaining //= factor
            exponent += 1
            power *= factor
        if exponent:
            term = power // factor * (factor - 1)
            if factor == 2 and exponent >= 3:
                term //= 2
            result = lcm(result, term)
        factor += 1
    if remaining > 1:
        result = lcm(result, remaining - 1)
    return result
