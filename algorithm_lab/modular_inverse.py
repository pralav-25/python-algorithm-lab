"""Extended-Euclidean modular inverses.

Accept signed integers and modulus >= 2; reject booleans and non-coprime
inputs. Return the unique inverse in [0, modulus). O(log modulus) Euclidean
steps and O(1) integers of auxiliary storage.

>>> modular_inverse(-3, 11)
7
"""

from algorithm_lab._validation import integer


def modular_inverse(value, modulus):
    integer(value)
    integer(modulus, "modulus", minimum=2)
    old_r, r, old_s, s = modulus, value % modulus, 0, 1
    while r:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
    if old_r != 1:
        raise ValueError("value and modulus must be coprime")
    return old_s % modulus
