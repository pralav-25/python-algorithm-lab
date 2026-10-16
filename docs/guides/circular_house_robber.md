# Choose nonadjacent houses on a circle to maximize their total value.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/circular_house_robber.py)

## Reasoning

The circular edge creates only one extra conflict: the first and last houses cannot both be selected. Solve the linear problem once with the first house excluded and once with the last excluded, then keep the better result.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.circular_house_robber import circular_house_robber

print(repr(circular_house_robber([2, 3, 2])))  # 3
```

## Boundary to remember

A single house may be taken, while the empty input returns zero. Values must be nonnegative integers, so taking no house never beats a positive option.

## Practice exercise

Choose the highest-value nonadjacent homes on a circular street, including the wraparound neighbor pair.
