# Merge two ordered sequences with minimal repetition

[Guide index](../README.md) · [Implementation](../../algorithm_lab/shortest_common_supersequence.py)

## Reasoning

A shared next character can be emitted once for both inputs. When next characters differ, choose the branch that leaves the shorter remaining supersequence. Dynamic programming records those remaining lengths, and reconstruction preserves the order of both original strings while allowing gaps.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.shortest_common_supersequence import shortest_common_supersequence
>>> answer = shortest_common_supersequence('ab', 'ba')
>>> answer
'aba'
>>> def contains_subsequence(whole, part):
...     remaining = iter(whole)
...     return all(any(item == wanted for item in remaining) for wanted in part)
>>> assert contains_subsequence(answer, 'ab') and contains_subsequence(answer, 'ba')
>>> shortest_common_supersequence('', 'task')
'task'

```

## Boundary to remember

Containment here means subsequence containment, not substring containment. Several shortest answers may exist; the implementation prefers the first input’s character on equal remaining lengths.
