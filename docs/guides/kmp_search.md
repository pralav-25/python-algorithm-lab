# Find overlapping text matches without rescanning

[Guide index](../README.md) · [Implementation](../../algorithm_lab/kmp_search.py)

## Reasoning

After a mismatch, the matched prefix tells us which shorter prefix could still be a suffix of the text already consumed. The prefix table stores these fallback lengths. Reusing that information prevents moving the text cursor backward and naturally supports overlapping occurrences.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.kmp_search import kmp_search
>>> text, pattern = "abababa", "aba"
>>> kmp_search(text, pattern)
[0, 2, 4]
>>> assert kmp_search(text, pattern) == [i for i in range(len(text)) if text.startswith(pattern, i)]
>>> kmp_search("xy", "")
[0, 1, 2]
>>> kmp_search("short", "longer")
[]

```

## Boundary to remember

Text is compared by Unicode code point. Case folding and normalization are separate preprocessing decisions; this implementation also treats an empty pattern as matching every boundary.
