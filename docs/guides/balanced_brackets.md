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

## Practice exercise

Two strings contain the same number of each bracket. Explain why only one is validly nested, and check both.

```pycon
>>> from collections import Counter
>>> from algorithm_lab.balanced_brackets import balanced_brackets
>>> valid, crossed = "{[()]}", "{[(])}"
>>> assert Counter(valid) == Counter(crossed)
>>> balanced_brackets(valid), balanced_brackets(crossed)
(True, False)

```

Character counts cannot certify nesting. In the crossed string, `]` arrives while `(` is the most recent unmatched opener; the stack exposes that mismatch.
