# Relabel a shrinking elimination circle

[Guide index](../README.md) · [Implementation](../../algorithm_lab/josephus.py)

## Reasoning

After one person is removed, the remaining circle is the same problem with one fewer participant and a shifted starting label. Translating the smaller problem’s survivor back into the original labels gives a simple recurrence. This avoids materializing every intermediate circle.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.josephus import josephus
>>> josephus(5, 2)
2
>>> circle, position = list(range(8)), 0
>>> while len(circle) > 1:
...     position = (position + 3 - 1) % len(circle)
...     circle.pop(position)
2
5
0
4
1
7
3
>>> assert josephus(8, 3) == circle[0] == 6
>>> josephus(1, 100)
0

```

## Boundary to remember

The returned label is zero-based and counting starts at person zero as count one. Off-by-one changes in either convention alter the survivor.
