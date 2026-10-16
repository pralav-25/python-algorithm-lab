# Count decodings of ASCII digits into the symbols numbered 1 through 26.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/decode_ways.py)

## Reasoning

Count decodings for each prefix. The final digit contributes when it is 1 through 9, and the final two digits contribute when they form a code from 10 through 26. Keeping only the last two prefix counts is enough to advance the recurrence.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.decode_ways import decode_ways

print(repr(decode_ways('226')))  # 3
```

## Boundary to remember

A zero cannot stand alone, and leading-zero pairs are invalid. The empty string has one empty decoding, which is useful as the recurrence's base case.

## Practice exercise

Count how many letter sequences can represent a numeric message such as 226.
