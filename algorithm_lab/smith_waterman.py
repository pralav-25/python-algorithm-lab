"""Return the optimal local alignment score with linear gap penalties.

Inputs are strings compared by literal Unicode code points. Match score must be
a positive integer; mismatch and gap scores must be nonpositive integers. Bool
is rejected for scores. An empty local alignment scores zero. Return only the
maximum score, so tied alignments need no selection. O(n*m+n+m) time and O(m+1) space
for string lengths n and m, excluding integer arithmetic; inputs are unchanged.

>>> smith_waterman('GGTTGACTA', 'TGTTACGG')
9
"""

from algorithm_lab._validation import integer


def smith_waterman(first: str, second: str, *, match=2, mismatch=-1, gap=-1) -> int:
    if not isinstance(first, str) or not isinstance(second, str):
        raise ValueError("both inputs must be strings")
    integer(match, "match", minimum=1)
    integer(mismatch, "mismatch")
    integer(gap, "gap")
    if mismatch > 0 or gap > 0:
        raise ValueError("mismatch and gap must be nonpositive")
    previous = [0] * (len(second) + 1)
    best = 0
    for char in first:
        current = [0] * (len(second) + 1)
        for column, other in enumerate(second, 1):
            current[column] = max(
                0,
                previous[column - 1] + (match if char == other else mismatch),
                previous[column] + gap,
                current[column - 1] + gap,
            )
            best = max(best, current[column])
        previous = current
    return best
