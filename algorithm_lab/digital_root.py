"""Reduce an integer's digits repeatedly to one digit in a chosen base.

value is an integer and base is an integer >=2, both excluding bool. Ignore the
sign and return a digit from 0 through base-1; zero returns 0. There are no ties.
The congruence formula uses O(1) arithmetic steps and integer storage, excluding
arbitrary-precision division costs.

>>> digital_root(-9875)
2
>>> digital_root(16, 2)
1
"""

from algorithm_lab._validation import integer


def digital_root(value, base=10):
    integer(value, "value")
    integer(base, "base", minimum=2)
    magnitude = abs(value)
    return 0 if magnitude == 0 else 1 + (magnitude - 1) % (base - 1)
