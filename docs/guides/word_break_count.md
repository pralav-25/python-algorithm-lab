# Count segmentations of text into dictionary words.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/word_break_count.py)

## Reasoning

Let each prefix count the number of dictionary segmentations ending there. For every reachable prefix, test dictionary words beginning at that boundary and add its count to the corresponding later prefix.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.word_break_count import word_break_count

print(repr(word_break_count('aaaa', ['a', 'aa', 'aa'])))  # 5
```

## Boundary to remember

Dictionary words must be nonempty, and duplicates are deduplicated so they do not create duplicate segmentations. Empty text has one empty segmentation.

## Practice exercise

Count the ways a repeated-character string can be split into words when the dictionary contains overlapping choices.
