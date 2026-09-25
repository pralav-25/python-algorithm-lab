"""Evaluate integer recurrences with a companion matrix.

initial and coefficients are nonempty equally sized integer sequences.
For k terms, a[n] = c[0]*a[n-1] + ... + c[k-1]*a[n-k]. n >= 0 is an
integer; bool is rejected throughout. O(k^3 log(n+1)) arithmetic operations
and O(k^2) space. Return an exact integer without modifying inputs.

>>> linear_recurrence([0, 1], [1, 1], 10)
55
"""

from algorithm_lab._validation import integer
from algorithm_lab.matrix_power import matrix_power


def linear_recurrence(initial, coefficients, n):
    integer(n, "n", minimum=0)
    initial, coefficients = list(initial), list(coefficients)
    k = len(initial)
    if not k or len(coefficients) != k:
        raise ValueError("initial values and coefficients must have the same positive length")
    for value in initial + coefficients:
        integer(value)
    if n < k:
        return initial[n]
    matrix = [coefficients] + [[int(j == i - 1) for j in range(k)] for i in range(1, k)]
    power = matrix_power(matrix, n - k + 1)
    return sum(power[0][j] * initial[k - 1 - j] for j in range(k))
