# Reassign earlier choices to maximize compatible pairs

[Guide index](../README.md) · [Implementation](../../algorithm_lab/bipartite_matching.py)

## Reasoning

A greedy choice can block a later left vertex even when a full matching
exists. An augmenting path alternates between unused edges and existing pairs,
then flips those choices to increase the matching size by one. Iterative
searches cost O(L(V + E)) time, where L is the number of left vertices. This
maximizes the number of pairs, without attaching scores to individual pairs.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.bipartite_matching import bipartite_matching
>>> skills = {"Ada": ["database", "web"], "Bo": ["database"], "Cy": []}
>>> pairs = bipartite_matching(skills)
>>> pairs == {"Ada": "web", "Bo": "database"}
True
>>> len(set(pairs.values())) == len(pairs)
True
>>> bipartite_matching({0: [0], 1: [1]})
{0: 0, 1: 1}

```

## Boundary to remember

Left and right labels occupy separate namespaces, so the same label can
appear on both sides. Unmatched left vertices are omitted. Duplicate edges
collapse, and traversal order resolves ties between maximum matchings.
[Stable matching](stable_matching.md) solves a different preference-based task.
