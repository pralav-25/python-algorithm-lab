"""Evaluate the Jacobi symbol (value/modulus) by quadratic reciprocity.

value is any integer; modulus is a positive odd integer; bool is excluded.
Return -1, 0, or 1, with (value/1)=1. A value of 1 need not mean a quadratic
residue for a composite modulus. There are no ties. O(log(modulus)) division
steps and O(1) integer storage, excluding arbitrary-precision costs.

>>> jacobi_symbol(5, 9)
1
>>> jacobi_symbol(3, 9)
0
"""

from algorithm_lab._validation import integer


def jacobi_symbol(value, modulus):
    integer(value, "value")
    integer(modulus, "modulus", minimum=1)
    if modulus % 2 == 0:
        raise ValueError("modulus must be odd")
    value %= modulus
    result = 1
    while value:
        while value % 2 == 0:
            value //= 2
            if modulus % 8 in (3, 5):
                result = -result
        value, modulus = modulus, value
        if value % 4 == modulus % 4 == 3:
            result = -result
        value %= modulus
    return result if modulus == 1 else 0
