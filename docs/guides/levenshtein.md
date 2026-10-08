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

## Practice exercise

Suggest candidate labels within one edit of cart. Independently generate all permitted one-edit results to check the filter.

```pycon
>>> from algorithm_lab.levenshtein import levenshtein
>>> source = "cart"
>>> candidates = ["cat", "coat", "chart", "cast", "carpet"]
>>> alphabet = set("".join(candidates))
>>> neighbors = {source}
>>> neighbors |= {source[:i] + source[i + 1 :] for i in range(len(source))}
>>> neighbors |= {source[:i] + char + source[i + 1 :] for i in range(len(source)) for char in alphabet}
>>> neighbors |= {source[:i] + char + source[i:] for i in range(len(source) + 1) for char in alphabet}
>>> suggestions = [word for word in candidates if levenshtein(source, word) <= 1]
>>> suggestions
['cat', 'chart', 'cast']
>>> assert suggestions == [word for word in candidates if word in neighbors]

```

The independent neighborhood contains deletions, substitutions, and insertions, plus the unchanged source. Its finite alphabet suffices because every candidate character is included. Adjacent transpositions are absent from both this neighborhood and the unit-cost edit model.
