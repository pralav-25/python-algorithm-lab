# Count insertions, deletions, and substitutions

[Guide index](../README.md) · [Implementation](../../algorithm_lab/levenshtein.py)

## Reasoning

Each dynamic-programming cell asks how to transform one prefix into another. Its last operation is an insertion, deletion, or aligned character comparison, so only neighboring cells are needed. Keeping the previous row instead of the whole table reduces memory when only the distance is required.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.levenshtein import levenshtein
>>> levenshtein("plane", "plans")
1
>>> levenshtein("ab", "ba")
2
>>> assert levenshtein("book", "back") == levenshtein("back", "book") == 2
>>> levenshtein("", "hello")
5

```

## Boundary to remember

Swapping adjacent characters costs two edits in this model, not one. A distance is also not an alignment; use edit_script when you need the actual sequence of operations.
