"""Return the number of k-element subsets of an n-element set.

n and k must be nonnegative integers, excluding booleans. k > n returns zero.
Use symmetry and exact incremental division: O(min(k, n-k)) arithmetic steps,
with a constant number of big integers. No floating-point arithmetic is used.

>>> binomial_coefficient(10, 3)
120
"""


def binomial_coefficient(n: int, k: int) -> int:
    if any(isinstance(x, bool) or not isinstance(x, int) or x < 0 for x in (n, k)):
        raise ValueError("n and k must be nonnegative integers")
    if k > n:
        return 0
    k = min(k, n - k)
    result = 1
    for step in range(1, k + 1):
        result = result * (n - k + step) // step
    return result
