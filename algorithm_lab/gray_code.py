"""Yield all bit-width integers in binary-reflected Gray-code order.

Consecutive outputs, including last-to-first for bits>0, differ in one bit.
Zero bits yields just 0. O(2**bits) integer operations, O(1) integer slots;
bit-operation costs grow with width. Validation happens before iteration.

>>> list(gray_code(3))
[0, 1, 3, 2, 6, 7, 5, 4]
"""

from algorithm_lab._validation import integer


def gray_code(bits):
    integer(bits, "bits", minimum=0)
    return (value ^ (value >> 1) for value in range(1 << bits))
