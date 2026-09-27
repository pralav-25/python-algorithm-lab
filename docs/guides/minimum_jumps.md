# Advance through layers of reachable positions

[Guide index](../README.md) · [Implementation](../../algorithm_lab/minimum_jumps.py)

## Reasoning

Every position reachable with the current number of jumps belongs to one breadth-first layer. Scanning that layer computes the farthest position reachable with one more jump. When the layer ends, advance to the next boundary rather than exploring every individual path.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.minimum_jumps import minimum_jumps
>>> minimum_jumps([3, 1, 1, 1, 1])
2
>>> minimum_jumps([1, 0, 2]) is None
True
>>> minimum_jumps([2, 0, 1])
1
>>> minimum_jumps([]), minimum_jumps([0])
(0, 0)

```

## Boundary to remember

Each number is a maximum jump length, so shorter jumps are permitted. A zero blocks progress only when no earlier position can jump beyond it.
