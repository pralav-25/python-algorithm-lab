"""Exact polynomial long division over rational coefficients.

Inputs contain int or Fraction coefficients in increasing degree order;
bool and floats are rejected. Return (quotient, remainder), both canonical
Fraction lists with [] representing zero. A zero divisor raises ValueError.
O(n*m) rational operations and O(n+m) space for degrees n and m.

>>> polynomial_divmod([-1, 0, 1], [-1, 1])
([Fraction(1, 1), Fraction(1, 1)], [])
"""

from fractions import Fraction


def polynomial_divmod(dividend, divisor):
    def convert(values):
        result = []
        for value in values:
            if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
                raise ValueError("coefficients must be integers or Fractions")
            result.append(Fraction(value))
        while result and result[-1] == 0:
            result.pop()
        return result

    remainder, divisor = convert(dividend), convert(divisor)
    if not divisor:
        raise ValueError("divisor must be nonzero")
    quotient = [Fraction(0)] * max(0, len(remainder) - len(divisor) + 1)
    while remainder and len(remainder) >= len(divisor):
        shift = len(remainder) - len(divisor)
        factor = remainder[-1] / divisor[-1]
        quotient[shift] = factor
        for i, coefficient in enumerate(divisor):
            remainder[i + shift] -= factor * coefficient
        while remainder and remainder[-1] == 0:
            remainder.pop()
    return quotient, remainder
