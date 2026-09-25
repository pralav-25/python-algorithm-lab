"""Exact floor roots using integer binary search.

value >= 0 and degree >= 1 are integers excluding bool. Return r satisfying
r**degree <= value < (r+1)**degree, without floats. O(bit_length(value))
comparisons, each using integer exponentiation; O(1) big integers stored.

>>> integer_nth_root(1000, 3)
10
"""

from algorithm_lab._validation import integer


def integer_nth_root(value, degree):
    integer(value, minimum=0)
    integer(degree, "degree", minimum=1)
    if value < 2 or degree == 1:
        return value
    if degree >= value.bit_length():
        return 1
    low, high = 0, 1 << ((value.bit_length() + degree - 1) // degree)
    while low + 1 < high:
        middle = (low + high) // 2
        if middle**degree <= value:
            low = middle
        else:
            high = middle
    return high if high**degree <= value else low
