# Decode a rank into one ordered arrangement

[Guide index](../README.md) · [Implementation](../../algorithm_lab/permutation_unrank.py)

## Reasoning

Divide the rank by the factorial block size to choose the next unused value. The remainder identifies the rank within that block, so repeating the division reconstructs the whole permutation. A sorted list of unused values gives a simple quadratic implementation.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.permutation_unrank import permutation_unrank
>>> from itertools import permutations
>>> orders = list(permutations(range(4)))
>>> assert all(tuple(permutation_unrank(4, rank)) == order for rank, order in enumerate(orders))
>>> permutation_unrank(4, 23)
[3, 2, 1, 0]
>>> permutation_unrank(0, 0)
[]

```

## Boundary to remember

The output is a permutation of range(n), not the caller’s own labels. Map indices back to labels afterward if the application uses named objects.

## Practice exercise

Recover the task ordering at rank thirty-one in a five-label alphabet,
checking it with a lazy standard-library permutation iterator.

```pycon
>>> from algorithm_lab.permutation_unrank import permutation_unrank
>>> from itertools import islice, permutations
>>> labels = ["audit", "build", "check", "deploy", "email"]
>>> rank = 31
>>> indices = permutation_unrank(len(labels), rank)
>>> indices
[1, 2, 0, 4, 3]
>>> ordering = tuple(labels[index] for index in indices)
>>> ordering
('build', 'check', 'audit', 'email', 'deploy')
>>> assert ordering == next(islice(permutations(labels), rank, rank + 1))

```

The first index selects the second block of twenty-four arrangements;
the remainder selects a block of six among the unused labels. Mapping
indices back through the same alphabet preserves the rank's meaning.
