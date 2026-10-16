# Return the exponent of a prime in n! using Legendre's formula.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/legendre_exponent.py)

## Reasoning

Count multiples of p in n!, then multiples of p squared, p cubed, and so on. Each higher power contributes an extra factor that the lower count did not include, so summing the floors gives the full exponent.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.legendre_exponent import legendre_exponent

print(repr(legendre_exponent(10, 2)))  # 8
```

## Boundary to remember

The second argument must be prime, not merely an integer greater than one. Zero factorial has exponent zero for every valid prime.

## Practice exercise

Find how many times a prime factor appears in a factorial before simplifying a binomial coefficient.
