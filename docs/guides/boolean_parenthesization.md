# Count false and true evaluations over all full parenthesizations.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/boolean_parenthesization.py)

## Reasoning

For every substring, keep two counts: parenthesizations that evaluate false and those that evaluate true. Splitting at each operator combines the left and right counts according to that operator, so the algorithm counts all binary tree shapes rather than applying ordinary precedence.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.boolean_parenthesization import boolean_parenthesization

print(repr(boolean_parenthesization('T|F&T')))  # (0, 2)
```

## Boundary to remember

The input must alternate T/F literals and &, |, or ^ operators. An empty expression has no literal and returns zero ways for both results.

## Practice exercise

Count how many ways a short Boolean expression can evaluate true when every legal parenthesization is allowed.
