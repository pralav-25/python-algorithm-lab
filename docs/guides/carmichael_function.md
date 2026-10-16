# Return the exponent of the multiplicative group modulo n.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/carmichael_function.py)

## Reasoning

The exponent of the full unit group can be computed from prime-power factors of the modulus. Factorization reduces the problem to known prime-power cases, and the least common multiple combines those independent exponents.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.carmichael_function import carmichael_function

print(repr(carmichael_function(8)))  # 2
```

## Boundary to remember

The function is defined here for every positive modulus, including lambda(1)=1. It is not the same as Euler's totient for many composite moduli.

## Practice exercise

Compare the exponents of the unit groups modulo 8 and 15 before using repeated modular powers.
