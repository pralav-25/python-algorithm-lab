"""Return F(n), with F(0)=0 and F(1)=1, using exact integers.

n must be a nonnegative integer, excluding booleans. The algorithm uses O(log(n+1))
doubling steps; arithmetic cost grows with the output's bit length. Iterative
execution uses a constant number of big integers, plus the binary index string.

>>> fast_fibonacci(10)
55
"""


def fast_fibonacci(n: int) -> int:
    if isinstance(n, bool) or not isinstance(n, int) or n < 0:
        raise ValueError("n must be a nonnegative integer")
    current, following = 0, 1
    for bit in bin(n)[2:]:
        even = current * (2 * following - current)
        odd = current * current + following * following
        current, following = (even, odd) if bit == "0" else (odd, even + odd)
    return current
