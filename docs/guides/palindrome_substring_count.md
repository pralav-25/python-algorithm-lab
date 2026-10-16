# Count nonempty palindromic substrings by their start and end positions.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/palindrome_substring_count.py)

## Reasoning

Every palindrome has either one center character or a gap between two center characters. Expand outwards from both kinds of centers and count each matching radius as another occurrence.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.palindrome_substring_count import palindrome_substring_count

print(repr(palindrome_substring_count('aaa')))  # 6
```

## Boundary to remember

Occurrences are counted by position, not by distinct substring value: the three single-character palindromes in 'aaa' are separate. Empty text contributes zero.

## Practice exercise

Count all palindromic ranges in a short word, including repeated single-character occurrences.
