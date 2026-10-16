# Format an integer in base 2 through 36 without a prefix.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/base_conversion.py)

## Reasoning

Repeated division by the destination base exposes one remainder at a time, starting with the least significant digit. Reversing those remainders restores positional order; the sign can be handled separately so the digit loop only sees a nonnegative magnitude.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.base_conversion import base_conversion

print(repr(base_conversion(-255, 16)))  # '-ff'
```

## Boundary to remember

Bases are limited to 2 through 36, and digits above nine use lowercase letters. Zero needs a special result because repeated division would otherwise produce no remainders.

## Practice exercise

Format a negative byte value in hexadecimal and compare it with the positive magnitude's representation.
