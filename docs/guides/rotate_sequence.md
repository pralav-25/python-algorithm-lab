# Return a new list rotated right by an integer number of steps.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/rotate_sequence.py)

## Reasoning

Normalize the requested shift modulo the sequence length, then split once at the new boundary and concatenate the two slices. Modulo handles shifts larger than the input and converts negative values into left rotations.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.rotate_sequence import rotate_sequence

print(repr(rotate_sequence([1, 2, 3, 4], 1)))  # [4, 1, 2, 3]
```

## Boundary to remember

An empty sequence returns an empty list, and the input is never mutated. Duplicate values keep their relative order through the rotation.

## Practice exercise

Rotate a queue snapshot by a large positive or negative step without moving the original data.
