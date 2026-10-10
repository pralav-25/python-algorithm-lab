"""Sum the base-b digits of the absolute value of an integer.

value is an integer and base is an integer >=2, both excluding bool. Return an
integer; zero has digit sum 0 and the sign is ignored. There are no ties.
Repeated division takes O(log_base(abs(value)+1)) arithmetic steps and O(1)
integers of storage, excluding arbitrary-precision costs.

>>> digit_sum(-12345)
15
>>> digit_sum(15, 2)
4
"""

from algorithm_lab._validation import integer


def digit_sum(value, base=10):
    integer(value, "value")
    integer(base, "base", minimum=2)
    remaining, result = abs(value), 0
    while remaining:
        remaining, digit = divmod(remaining, base)
        result += digit
    return result
