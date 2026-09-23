"""Return (g, x, y) with g = gcd(a, b) >= 0 and a*x + b*y = g.

For (0, 0), return (0, 1, 0). Inputs must be integers, excluding booleans.
Euclid uses O(log(max(abs(a), abs(b)) + 1)) iterations and a constant number of
integer variables; arithmetic costs depend on operand size.

>>> extended_gcd(30, 18)
(6, -1, 2)
"""


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    if any(isinstance(value, bool) or not isinstance(value, int) for value in (a, b)):
        raise ValueError("arguments must be integers")
    old_r, r, old_x, x, old_y, y = abs(a), abs(b), 1, 0, 0, 1
    while r:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_x, x = x, old_x - quotient * x
        old_y, y = y, old_y - quotient * y
    return old_r, old_x if a >= 0 else -old_x, old_y if b >= 0 else -old_y
