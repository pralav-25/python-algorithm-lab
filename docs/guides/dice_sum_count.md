# Count ordered outcomes of identical numbered dice with a given total.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/dice_sum_count.py)

## Reasoning

Build counts by adding one die at a time. Each new total receives contributions from the previous row's totals one through faces steps below it; a rolling row avoids storing every intermediate dice count.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.dice_sum_count import dice_sum_count

print(repr(dice_sum_count(2, 6, 7)))  # 6
```

## Boundary to remember

Dice are ordered, so swapping outcomes between two dice creates a different outcome. Zero dice has exactly one outcome for total zero and none for other totals.

## Practice exercise

Count the ordered rolls of a small number of standard dice that reach a specified sum.
