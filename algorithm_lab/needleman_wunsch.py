"""Return the optimal global alignment score with linear gap penalties.

Inputs must be strings, compared by literal Unicode code points. Match,
mismatch and gap scores are arbitrary integers, excluding bool. Each alignment
column has two characters or one character and a gap, never two gaps. Every
character is used. Empty inputs score their required gaps. Return only the best
integer score, so ties need no selection. O(n*m+n+m) time and O(m+1) space excluding
integer arithmetic; inputs are unchanged.

>>> needleman_wunsch('GATTACA', 'GCATGCU')
0
"""

from algorithm_lab._validation import integer


def needleman_wunsch(first: str, second: str, *, match=1, mismatch=-1, gap=-1) -> int:
    if not isinstance(first, str) or not isinstance(second, str):
        raise ValueError("both inputs must be strings")
    for name, value in (("match", match), ("mismatch", mismatch), ("gap", gap)):
        integer(value, name)
    previous = [column * gap for column in range(len(second) + 1)]
    for row, char in enumerate(first, 1):
        current = [row * gap] + [0] * len(second)
        for column, other in enumerate(second, 1):
            current[column] = max(
                previous[column - 1] + (match if char == other else mismatch),
                previous[column] + gap,
                current[column - 1] + gap,
            )
        previous = current
    return previous[-1]
