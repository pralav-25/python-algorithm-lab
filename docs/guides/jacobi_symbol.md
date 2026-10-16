# Evaluate the Jacobi symbol (value/modulus) by quadratic reciprocity.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/jacobi_symbol.py)

## Reasoning

Remove powers of two using the supplementary sign rule, then swap numerator and denominator using quadratic reciprocity. Repeating this Euclidean-style reduction keeps the values small while accumulating the final sign.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.jacobi_symbol import jacobi_symbol

print(repr(jacobi_symbol(5, 9)))  # 1
```

## Boundary to remember

The modulus must be positive and odd. For a composite modulus, a Jacobi value of one does not prove that the numerator is a quadratic residue.

## Practice exercise

Evaluate a Jacobi symbol modulo an odd composite and explain why its value is not a primality certificate.
