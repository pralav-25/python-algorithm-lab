# Exponentiate while keeping intermediate values bounded

[Guide index](../README.md) · [Implementation](../../algorithm_lab/modular_power.py)

## Reasoning

Read the exponent in binary. Squaring advances to the next power of two, while multiplying only on set bits accumulates the requested power. Reducing modulo the modulus after each multiplication preserves the final remainder without constructing an enormous full integer power.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.modular_power import modular_power
>>> modular_power(7, 20, 13)
3
>>> assert modular_power(-17, 123, 97) == pow(-17, 123, 97)
>>> modular_power(9, 0, 1)
0
>>> modular_power(0, 5, 11)
0

```

## Boundary to remember

This implementation accepts nonnegative exponents only and requires a positive modulus. Arithmetic is exact, but the running time still depends on the size of the modulus as well as the exponent bits.

## Practice exercise

Compute the final three decimal digits of a power and verify the
exponent-addition identity using two smaller powers.

```pycon
>>> from algorithm_lab.modular_power import modular_power
>>> remainder = modular_power(3, 15, 1000)
>>> remainder
907
>>> assert remainder == (3**15) % 1000
>>> assert remainder == modular_power(3, 7, 1000) * modular_power(3, 8, 1000) % 1000
>>> assert modular_power(3, 10**6, 1000) == pow(3, 10**6, 1000)

```

The modulus keeps exactly the last three digits even as the unreduced
power grows. Splitting fifteen into seven plus eight multiplies residues,
whereas splitting the exponent's binary digits drives repeated squaring.
