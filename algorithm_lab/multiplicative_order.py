"""Find the order of an invertible residue.

value is an integer and modulus >= 2, excluding bool. Reject non-coprime
inputs. Return the smallest positive k with value**k == 1 modulo modulus.
This educational repeated-multiplication method takes O(modulus) modular
multiplications and O(1) integers of storage.

>>> multiplicative_order(2, 7)
3
"""

from math import gcd

from algorithm_lab._validation import integer


def multiplicative_order(value, modulus):
    integer(value)
    integer(modulus, "modulus", minimum=2)
    if gcd(value, modulus) != 1:
        raise ValueError("value and modulus must be coprime")
    residue, order = value % modulus, 1
    current = residue
    while current != 1:
        current = current * residue % modulus
        order += 1
    return order
