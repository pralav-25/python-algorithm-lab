"""Count derangements of n distinct elements; D(0)=1 and D(1)=0.

Uses D(n)=(n-1)*(D(n-1)+D(n-2)): O(n) arithmetic operations, O(1) integer slots.
Big-integer sizes grow with n. n must be a nonnegative integer, excluding bool.

>>> [derangements(n) for n in range(6)]
[1, 0, 1, 2, 9, 44]
"""

from algorithm_lab._validation import integer


def derangements(n):
    integer(n, "n", minimum=0)
    if n == 0:
        return 1
    previous, current = 1, 0
    for size in range(2, n + 1):
        previous, current = current, (size - 1) * (previous + current)
    return current
