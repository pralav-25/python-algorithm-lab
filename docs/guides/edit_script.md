# Return the operations behind an edit distance

[Guide index](../README.md) · [Implementation](../../algorithm_lab/edit_script.py)

## Reasoning

The Levenshtein table stores an optimal cost for each pair of prefixes. Tracing backward through an optimal predecessor recovers a character alignment with equal, replacement, insertion, and deletion operations. The alignment itself supplies two checks: its source characters reconstruct the source and its target characters reconstruct the target.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.edit_script import edit_script
>>> source, target = "stone", "tones"
>>> distance, operations = edit_script(source, target)
>>> distance
2
>>> assert "".join(left for kind, left, right in operations) == source
>>> assert "".join(right for kind, left, right in operations) == target
>>> assert sum(kind != "equal" for kind, left, right in operations) == distance

```

## Boundary to remember

Operation tuples describe aligned characters rather than mutable-string offsets. Applying them as index edits to a changing buffer would require a separate cursor convention.
