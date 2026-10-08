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

## Practice exercise

For elimination step two, verify the survivor against the closed-form rule and translate the zero-based result back to a participant's label.

```pycon
>>> from algorithm_lab.josephus import josephus
>>> survivors = [josephus(size, 2) for size in range(8, 13)]
>>> survivors
[0, 2, 4, 6, 8]
>>> for size in range(1, 17):
...     largest_power_of_two = 1 << (size.bit_length() - 1)
...     assert josephus(size, 2) == 2 * (size - largest_power_of_two)
>>> participants = list("ABCDEFGHIJK")
>>> participants[josephus(len(participants), 2)]
'G'

```

For step two, a power-of-two circle returns survivor zero; each added participant shifts the survivor by two until the next power-of-two reset. The rule is specific to step two. Indexing the participant list directly avoids an accidental one-based label conversion.
