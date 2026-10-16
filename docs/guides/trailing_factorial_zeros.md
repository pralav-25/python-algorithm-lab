# Count trailing zero digits of n! represented in an arbitrary base.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/trailing_factorial_zeros.py)

## Reasoning

Factor the output base into primes. For each prime, Legendre's formula counts its exponent in n!; the number of complete base factors is limited by the least exponent-to-base requirement ratio.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.trailing_factorial_zeros import trailing_factorial_zeros

print(repr(trailing_factorial_zeros(10)))  # 2
```

## Boundary to remember

The base may be any integer at least two, not just ten. The answer counts complete trailing zero digits in that base, and 0! has none.

## Practice exercise

Count the trailing zero digits of a factorial when it is written in a base other than ten.
