# Store the minimum alongside each stack prefix

[Guide index](../README.md) · [Implementation](../../algorithm_lab/min_stack.py)

## Reasoning

Every pushed entry stores its own value and the minimum of the entire
stack ending at that entry. Popping automatically exposes the preceding
prefix's minimum, so no rescanning is needed. Push, pop, peek, and minimum
each take O(1) time with O(n) total space. Keeping prefix minima also handles
duplicate smallest values correctly.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.min_stack import MinStack
>>> stack = MinStack()
>>> for value in [5, 2, 2, 7]:
...     stack.push(value)
>>> stack.peek(), stack.minimum()
(7, 2)
>>> stack.pop(), stack.pop(), stack.minimum()
(7, 2, 2)
>>> stack.pop(), stack.minimum()
(2, 5)

```

## Boundary to remember

Values must share a consistent total order; NaN is unsupported. Empty
pop, peek, or minimum operations raise IndexError. The minimum describes the
whole current stack, while peek returns just its newest item. Removing one
copy of a duplicate minimum does not remove the other.

## Practice exercise

Use tuple priorities in a stack, then remove entries until an older
minimum becomes visible again.

```pycon
>>> from algorithm_lab.min_stack import MinStack
>>> priorities = MinStack()
>>> for value in [("b", 2), ("a", 3), ("a", 1), ("c", 0)]:
...     priorities.push(value)
>>> priorities.minimum()
('a', 1)
>>> priorities.pop(), priorities.pop()
(('c', 0), ('a', 1))
>>> priorities.peek(), priorities.minimum(), len(priorities)
(('a', 3), ('a', 3), 2)

```

Tuple comparison is lexicographic: the second component matters only
when the first matches. Each stored prefix minimum must restore the
older tuple when the newer minimum is popped.
