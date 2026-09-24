"""Find an element occurring more than n/2 times, or raise ValueError.

Requires a re-iterable sequence with equality-comparable elements; None is a
valid majority. O(n) time, O(1) auxiliary space. A second pass rejects candidates
that are only a plurality, including on empty input.

>>> majority_element([2, 1, 2, 2])
2
"""


def majority_element(values):
    candidate, balance = None, 0
    for value in values:
        if balance == 0:
            candidate = value
        balance += 1 if value == candidate else -1
    if sum(value == candidate for value in values) <= len(values) // 2:
        raise ValueError("no strict majority")
    return candidate
