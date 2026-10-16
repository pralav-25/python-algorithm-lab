# Decide whether a string interleaves two strings in their original order.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/interleaving_strings.py)

## Reasoning

A prefix of the result is reachable if its final character came from the next unused character of either source and the preceding prefix was reachable. A two-dimensional state describes the idea; one row suffices when updated in the right order.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.interleaving_strings import interleaving_strings

print(repr(interleaving_strings('ab', 'cd', 'acbd')))  # True
```

## Boundary to remember

Every source character must be used exactly once and source order is preserved. Matching uses literal Unicode code points, with no normalization or reordering.

## Practice exercise

Check whether two ordered message fragments could have produced one combined stream without changing either fragment's internal order.
