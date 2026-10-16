# Find the first match in ascending sorted data with square-root jumps.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/jump_search.py)

## Reasoning

Skip ahead by blocks of about square-root size until a block's last value reaches the target. Then scan only that block, balancing the number of jumps and the length of the final linear search.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.jump_search import jump_search

print(repr(jump_search([1, 3, 3, 7], 3)))  # 1
```

## Boundary to remember

The input must support random access and already be sorted in ascending order. The function assumes sortedness and returns the first duplicate occurrence.

## Practice exercise

Find a value in a sorted static table when a simple bounded number of comparisons is preferred over binary-search branching.
