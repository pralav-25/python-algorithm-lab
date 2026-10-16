# Count tilings of a 2-by-n rectangle with unlabelled 2-by-1 dominoes.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/domino_tilings.py)

## Reasoning

At the left edge of a 2-by-n board, either one vertical domino fills the first column or two horizontal dominoes fill the first two columns. Those cases leave widths n-1 and n-2, giving the Fibonacci-style recurrence.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.domino_tilings import domino_tilings

print(repr(domino_tilings(4)))  # 5
```

## Boundary to remember

Width zero contributes one empty tiling. Dominoes are indistinguishable, and rotations of the whole board are not identified as the same arrangement.

## Practice exercise

Count the coverings of a narrow hallway made from 2-by-1 tiles for several widths.
