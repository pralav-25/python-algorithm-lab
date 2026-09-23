"""Return floor(sqrt(value)) without floating-point conversion.

value must be a nonnegative integer, excluding booleans. The initial power-of-two
upper bound yields O(log(bit_length(value) + 1)) Newton iterations; division cost
depends on integer size. Only a constant number of big integers are stored.

>>> integer_sqrt(99)
9
>>> integer_sqrt(100)
10
"""


def integer_sqrt(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError("value must be a nonnegative integer")
    if value == 0:
        return 0
    estimate = 1 << ((value.bit_length() + 1) // 2)
    while True:
        improved = (estimate + value // estimate) // 2
        if improved >= estimate:
            return estimate
        estimate = improved
