"""Count trailing zero digits of n! represented in an arbitrary base.

n is a nonnegative integer and base is an integer >=2, both excluding bool.
Return the number of complete factors of base in n!, including 0 for 0!.
There are no ties. Trial division uses O(sqrt(base)+log(base)*log(n+1))
arithmetic steps and O(1) integer storage, excluding big-integer costs.

>>> trailing_factorial_zeros(10)
2
>>> trailing_factorial_zeros(10, 12)
4
"""

from algorithm_lab._validation import integer


def trailing_factorial_zeros(n, base=10):
    integer(n, "n", minimum=0)
    integer(base, "base", minimum=2)
    remaining, factor, result = base, 2, None
    while factor * factor <= remaining:
        if remaining % factor == 0:
            multiplicity = 0
            while remaining % factor == 0:
                remaining //= factor
                multiplicity += 1
            quotient, exponent = n, 0
            while quotient:
                quotient //= factor
                exponent += quotient
            zeros = exponent // multiplicity
            result = zeros if result is None else min(result, zeros)
        factor += 1
    if remaining > 1:
        quotient, exponent = n, 0
        while quotient:
            quotient //= remaining
            exponent += quotient
        result = exponent if result is None else min(result, exponent)
    return result
