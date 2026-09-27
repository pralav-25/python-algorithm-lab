# Check nested bracket structure with a stack

[Guide index](../README.md) · [Implementation](../../algorithm_lab/balanced_brackets.py)

## Reasoning

The most recently opened bracket is the only opener that the next closing bracket may match. A stack records that nesting order. Rejecting a mismatch immediately and requiring an empty stack at the end handles both crossed pairs and unfinished groups in one pass.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.balanced_brackets import balanced_brackets
>>> balanced_brackets("call({key: [1, 2]})")
True
>>> balanced_brackets("[(])")
False
>>> balanced_brackets("unfinished(")
False
>>> balanced_brackets("ordinary text")
True

```

## Boundary to remember

This is not a programming-language parser. Quoted text and comments receive no special treatment, so a bracket inside a string literal still participates in matching.
