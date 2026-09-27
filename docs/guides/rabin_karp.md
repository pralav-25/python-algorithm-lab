# Use rolling hashes without trusting collisions

[Guide index](../README.md) · [Implementation](../../algorithm_lab/rabin_karp.py)

## Reasoning

A rolling hash updates a window fingerprint by removing its leading character and adding its new trailing character. Equal fingerprints are candidates rather than proof: comparing the actual substring preserves correctness even when hashes collide. This is useful for understanding the difference between a fast filter and an exact predicate.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.rabin_karp import rabin_karp
>>> text, pattern = "mississippi", "issi"
>>> rabin_karp(text, pattern)
[1, 4]
>>> assert rabin_karp(text, pattern) == [i for i in range(len(text)) if text.startswith(pattern, i)]
>>> rabin_karp("abc", "xyz")
[]
>>> rabin_karp("", "")
[0]

```

## Boundary to remember

Frequent hash hits still require full substring verification, so the worst case is quadratic in text and pattern lengths. Overlaps are reported, and an empty pattern matches all boundaries.
