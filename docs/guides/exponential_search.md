# Find the first match in a sorted sequence by exponential bracketing.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/exponential_search.py)

## Reasoning

Double the upper index until it reaches or passes the target, creating a bracket that contains the first possible match. Binary search then works only inside that bracket, which is useful when the sequence is sorted but its length or target position is not known in advance.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.exponential_search import exponential_search

print(repr(exponential_search([1, 3, 3, 9], 3)))  # 1
```

## Boundary to remember

Ascending sortedness is a precondition and is not checked. Duplicate targets return the first occurrence, matching the repository's lower-bound convention.

## Practice exercise

Locate a timestamp in a sorted stream prefix when the likely position is near the beginning but the full range is not known.
