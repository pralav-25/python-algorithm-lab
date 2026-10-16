# Find the smallest primitive root of an integer modulus.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/primitive_root.py)

## Reasoning

A candidate generates all units modulo m when its powers avoid one for every proper divisor of phi(m). Factoring phi(m) reduces that check to one modular exponentiation per prime divisor, while testing candidates in order selects the least one.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.primitive_root import primitive_root

print(repr(primitive_root(7)))  # 3
```

## Boundary to remember

A primitive root exists only for certain moduli; the function returns None when the unit group is not cyclic. Modulus must be at least two.

## Practice exercise

Find the smallest generator modulo a prime and contrast it with a modulus that has no primitive root.
