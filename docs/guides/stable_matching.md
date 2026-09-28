# Resolve ranked preferences without blocking pairs

[Guide index](../README.md) · [Implementation](../../algorithm_lab/stable_matching.py)

## Reasoning

Free proposers approach receivers in preference order. Each receiver
keeps its preferred offer so far and rejects the other proposer, who continues
down its list. No proposer repeats a proposal, giving O(n squared) time.
The result is stable: no unmatched pair prefers each other to their assigned
partners. Among stable matchings, the outcome is optimal for the proposing side.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.stable_matching import stable_matching
>>> proposers = [[0, 1], [0, 1]]
>>> receivers = [[1, 0], [0, 1]]
>>> partners = stable_matching(proposers, receivers)
>>> partners
[1, 0]
>>> receivers[0].index(1) < receivers[0].index(0)
True
>>> stable_matching([], [])
[]

```

## Boundary to remember

Each side supplies a complete n-by-n strict ranking: every row must be a
permutation of range(n). Returned position p contains proposer p's receiver.
Stability is not maximum total satisfaction, and switching the proposing side
can change the outcome. For compatibility without rankings compare
[bipartite matching](bipartite_matching.md).
