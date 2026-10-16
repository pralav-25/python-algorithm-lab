# Choose nonadjacent houses on a line to maximize their total value.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/house_robber.py)

## Reasoning

For each house, compare skipping it with taking it plus the best result that ends two positions earlier. The state only needs the previous two optima, so a full table is unnecessary.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.house_robber import house_robber

print(repr(house_robber([2, 7, 9, 3, 1])))  # 12
```

## Boundary to remember

Taking no houses is allowed, making zero the result for empty input and for all-zero values. Adjacent houses cannot both be selected.

## Practice exercise

Choose a maximum-value set of nonadjacent entries along a line of storage lockers.
