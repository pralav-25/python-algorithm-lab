"""Gale-Shapley matching with complete strict preferences.

Each side is an n-by-n matrix whose rows are permutations of range(n).
Integers exclude bool. Return the receiver index matched to each proposer.
Proposers offer in index order through a FIFO queue; the result is proposer
optimal. Empty inputs return []. O(n^2) time and space; inputs are unchanged.

>>> stable_matching([[0, 1], [0, 1]], [[1, 0], [0, 1]])
[1, 0]
"""

from collections import deque

from algorithm_lab._validation import integer


def stable_matching(proposers, receivers):
    proposers, receivers = [list(row) for row in proposers], [list(row) for row in receivers]
    n = len(proposers)
    if len(receivers) != n:
        raise ValueError("both sides must have equal size")
    for row in proposers + receivers:
        for value in row:
            integer(value)
        if len(row) != n or set(row) != set(range(n)):
            raise ValueError("each preference row must permute range(n)")
    ranks = [{p: rank for rank, p in enumerate(row)} for row in receivers]
    free, next_choice, partners, result = deque(range(n)), [0] * n, [-1] * n, [-1] * n
    while free:
        proposer = free.popleft()
        receiver = proposers[proposer][next_choice[proposer]]
        next_choice[proposer] += 1
        current = partners[receiver]
        if current == -1 or ranks[receiver][proposer] < ranks[receiver][current]:
            partners[receiver], result[proposer] = proposer, receiver
            if current != -1:
                result[current] = -1
                free.append(current)
        else:
            free.append(proposer)
    return result
