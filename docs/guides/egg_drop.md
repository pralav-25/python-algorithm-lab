# Return minimum worst-case drops needed to identify an egg-breaking floor.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/egg_drop.py)

## Reasoning

Instead of asking which floor to try first, ask how many floors can be distinguished with a given number of moves and eggs. One move either breaks an egg and leaves one fewer egg below, or survives and leaves the same eggs above; the two ranges add one tested floor.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.egg_drop import egg_drop

print(repr(egg_drop(2, 100)))  # 14
```

## Boundary to remember

At least one egg is required, and zero floors needs zero drops. The answer is a worst-case guarantee, not the expected number of attempts.

## Practice exercise

Find the minimum worst-case trial count for a building with two fragile sensors and one hundred levels.
