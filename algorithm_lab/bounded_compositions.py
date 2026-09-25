"""Enumerate fixed-sum tuples under per-position upper bounds.

total and each bound are nonnegative integers excluding bool. Yield tuples
in lexicographic order, with 0 <= value[i] <= bounds[i] and the given sum.
No bounds yields () only for total=0. An explicit stack avoids recursion;
O(k) working space, and O(k) work per yielded tuple plus visited prefixes.

>>> list(bounded_compositions(2, [1, 2]))
[(0, 2), (1, 1)]
"""

from algorithm_lab._validation import integer


def bounded_compositions(total, bounds):
    integer(total, "total", minimum=0)
    bounds = list(bounds)
    for bound in bounds:
        integer(bound, "bound", minimum=0)
    suffix = [0] * (len(bounds) + 1)
    for i in range(len(bounds) - 1, -1, -1):
        suffix[i] = suffix[i + 1] + bounds[i]
    if not bounds:
        if total == 0:
            yield ()
        return

    def choices(i, remaining):
        return iter(range(max(0, remaining - suffix[i + 1]), min(bounds[i], remaining) + 1))

    prefix = []
    stack = [(total, choices(0, total))]
    while stack:
        remaining, iterator = stack[-1]
        value = next(iterator, None)
        if value is None:
            stack.pop()
            if prefix:
                prefix.pop()
        elif len(stack) == len(bounds):
            yield tuple(prefix + [value])
        else:
            prefix.append(value)
            stack.append((remaining - value, choices(len(prefix), remaining - value)))
