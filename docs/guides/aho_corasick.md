# Search many patterns in a single pass

[Guide index](../README.md) · [Implementation](../../algorithm_lab/aho_corasick.py)

## Reasoning

A trie shares pattern prefixes, while failure links recover the longest suffix that could begin another pattern after a mismatch. Output links preserve patterns ending at the same state, including shorter patterns nested in longer ones. Searching can therefore report many overlapping matches during one text scan.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.aho_corasick import AhoCorasick
>>> patterns, text = ["aba", "ba", "aba"], "ababa"
>>> matches = AhoCorasick(patterns).find_all(text)
>>> len(matches)
6
>>> assert all(text[start:stop] == patterns[index] for start, stop, index in matches)
>>> sorted(start for start, stop, index in matches if index == 0)
[0, 2]
>>> AhoCorasick([]).find_all(text)
[]

```

## Boundary to remember

Pattern indices distinguish duplicate patterns. Matches with the same end position have no promised tie order, so sort results when a presentation requires a stable tuple ordering.

## Practice exercise

A log viewer highlights both whole error messages and warning prefixes. Find every highlight in `error warning error`, preserving the identity of the matched keyword.

```pycon
>>> from algorithm_lab.aho_corasick import AhoCorasick
>>> keywords = ["error", "warn"]
>>> highlights = sorted(AhoCorasick(keywords).find_all("error warning error"))
>>> highlights
[(0, 5, 0), (6, 10, 1), (14, 19, 0)]
>>> assert [keywords[index] for _, _, index in highlights] == ["error", "warn", "error"]

```

The stop offsets are excluded. Matching `warn` inside `warning` is intentional: the automaton finds substrings, so whole-word filtering belongs in the caller.
