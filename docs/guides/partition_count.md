# Count unordered integer partitions of n into positive parts.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/partition_count.py)

## Reasoning

Treat each possible part size like a coin and update totals in place. Iterating part sizes in one direction ensures that arrangements such as 1+2 and 2+1 are counted as the same unordered partition.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.partition_count import partition_count

print(repr(partition_count(7)))  # 15
```

## Boundary to remember

Parts are positive integers and order does not matter. The empty partition gives p(0)=1, which anchors the dynamic program.

## Practice exercise

Count the different unordered ways to split a small integer into positive pieces.
