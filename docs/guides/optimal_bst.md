# Minimize weighted successful-search comparisons in an ordered BST.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/optimal_bst.py)

## Reasoning

For every key interval, try each key as the root. Its left and right intervals become child trees, so all their frequencies gain one comparison level; prefix sums add that shared cost efficiently.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.optimal_bst import optimal_bst

print(repr(optimal_bst([34, 8, 50])))  # 142
```

## Boundary to remember

Only successful searches are weighted; unsuccessful searches have no cost in this model. Frequencies follow sorted key order, and the root comparison is depth one.

## Practice exercise

Choose a search-tree shape for ordered keys that receive very different query frequencies.
