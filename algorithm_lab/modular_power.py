"""Compute base**exponent modulo modulus without constructing the full power.

Arguments are integers excluding booleans; exponent >= 0 and modulus > 0.
Negative bases are supported. Work uses O(log(exponent + 1)) modular multiply
steps and a constant number of integers. Arithmetic costs depend on modulus size.

>>> modular_power(-3, 5, 7)
2
"""


def modular_power(base: int, exponent: int, modulus: int) -> int:
    if any(isinstance(x, bool) or not isinstance(x, int) for x in (base, exponent, modulus)):
        raise ValueError("arguments must be integers")
    if exponent < 0 or modulus <= 0:
        raise ValueError("exponent must be nonnegative and modulus positive")
    result, base = 1 % modulus, base % modulus
    while exponent:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result
