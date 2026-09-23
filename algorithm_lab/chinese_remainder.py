"""Return (smallest nonnegative solution, period) for modular constraints.

Each pair is (integer remainder, positive integer modulus), excluding booleans.
Non-coprime moduli are supported; inconsistent systems raise ValueError. Empty
constraints return (0, 1). Each merge runs extended Euclid; arithmetic and storage
cost grow with the combined modulus, which is the least common multiple.

>>> chinese_remainder([(2, 4), (6, 8)])
(6, 8)
>>> chinese_remainder([(2, 3), (3, 5), (2, 7)])
(23, 105)
"""

from algorithm_lab.extended_gcd import extended_gcd


def chinese_remainder(congruences) -> tuple[int, int]:
    result, period = 0, 1
    for remainder, modulus in congruences:
        if any(isinstance(x, bool) or not isinstance(x, int) for x in (remainder, modulus)):
            raise ValueError("remainders and moduli must be integers")
        if modulus <= 0:
            raise ValueError("moduli must be positive")
        divisor, inverse, _ = extended_gcd(period, modulus)
        difference = remainder - result
        if difference % divisor:
            raise ValueError("congruences are inconsistent")
        step = (difference // divisor * inverse) % (modulus // divisor)
        new_period = period // divisor * modulus
        result = (result + period * step) % new_period
        period = new_period
    return result, period
