# Enumerate primitive positive Pythagorean triples with bounded hypotenuse.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/pythagorean_triples.py)

## Reasoning

Euclid's formula constructs primitive right triangles from coprime integers m>n of opposite parity. The hypotenuse is m squared plus n squared, so bounding it limits the candidate search before the legs are formed.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.pythagorean_triples import pythagorean_triples

print(repr(pythagorean_triples(20)))  # [(3, 4, 5), (5, 12, 13), (8, 15, 17)]
```

## Boundary to remember

Only primitive positive triples are returned, with a<b and c within the inclusive limit. Scaling a primitive triple by a factor greater than one is deliberately excluded.

## Practice exercise

List the primitive right triangles whose hypotenuse does not exceed a small length limit.
