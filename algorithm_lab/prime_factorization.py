"""Factor a positive integer into a dict of prime -> exponent, in increasing order.

One has the empty factorization. Booleans, zero, and negative inputs are invalid.
Worst-case work is O(sqrt(n)) trial divisions; integer arithmetic has variable cost.
This teaching implementation is intended for modest inputs, not large semiprimes.

>>> prime_factorization(360)
{2: 3, 3: 2, 5: 1}
"""


def prime_factorization(value: int) -> dict[int, int]:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError("value must be a positive integer")
    factors = {}
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors[value] = factors.get(value, 0) + 1
    return factors
