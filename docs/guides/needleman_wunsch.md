# Return the optimal global alignment score with linear gap penalties.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/needleman_wunsch.py)

## Reasoning

Global alignment must consume every character from both strings. Each dynamic-programming cell considers a match or mismatch, a gap in the first string, or a gap in the second; the best score can be computed with one rolling row when no alignment is reconstructed.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.needleman_wunsch import needleman_wunsch

print(repr(needleman_wunsch('GATTACA', 'GCATGCU')))  # 0
```

## Boundary to remember

Gap penalties are linear and can be arbitrary integer scores. Empty input still incurs gaps for the other string, unlike local alignment where an empty match can score zero.

## Practice exercise

Score two complete DNA sequences when insertions and deletions should be represented as explicit gaps.
