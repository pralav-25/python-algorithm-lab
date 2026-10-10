"""Format an integer in base 2 through 36 without a prefix.

value is an integer and base is an integer from 2 through 36; bool is excluded.
Return a string using lowercase letters, a leading minus for negative values,
and '0' for zero. There are no ties. O(log_base(abs(value)+1)) arithmetic steps
and characters of storage, excluding arbitrary-precision division costs.

>>> base_conversion(-255, 16)
'-ff'
>>> base_conversion(35, 36)
'z'
"""

from algorithm_lab._validation import integer


def base_conversion(value, base=10):
    integer(value, "value")
    integer(base, "base", minimum=2)
    if base > 36:
        raise ValueError("base must be at most 36")
    if value == 0:
        return "0"
    remaining, digits = abs(value), []
    alphabet = "0123456789abcdefghijklmnopqrstuvwxyz"
    while remaining:
        remaining, digit = divmod(remaining, base)
        digits.append(alphabet[digit])
    return ("-" if value < 0 else "") + "".join(reversed(digits))
