# Count index selections whose characters form a target subsequence.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/target_subsequence_count.py)

## Reasoning

Maintain the number of ways to form each target prefix while scanning source characters. Update target positions from right to left so the current source character cannot be reused twice in one subsequence.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.target_subsequence_count import target_subsequence_count

print(repr(target_subsequence_count('rabbbit', 'rabbit')))  # 3
```

## Boundary to remember

Different source index selections count separately even when their characters are equal. The empty target has one matching selection, including for empty source text.

## Practice exercise

Count how many index selections in a repeated-character string spell a short target.
