"""Count ordered outcomes of identical numbered dice with a given total.

Dice and total are nonnegative integers, faces a positive integer; bool is
rejected. Each die has faces 1 through faces. Zero dice produces total zero
once and any other total zero times. Return an exact count; all tied outcomes
are counted. O(dice*total) time and O(total) auxiliary space excluding integer
arithmetic; no input mutation.

>>> dice_sum_count(2, 6, 7)
6
"""

from algorithm_lab._validation import integer


def dice_sum_count(dice: int, faces: int, total: int) -> int:
    integer(dice, "dice", minimum=0)
    integer(faces, "faces", minimum=1)
    integer(total, "total", minimum=0)
    if not dice:
        return int(total == 0)
    if total < dice or total > dice * faces:
        return 0
    counts = [1] + [0] * total
    for _ in range(dice):
        following = [0] * (total + 1)
        window = 0
        for amount in range(1, total + 1):
            window += counts[amount - 1]
            if amount > faces:
                window -= counts[amount - faces - 1]
            following[amount] = window
        counts = following
    return counts[total]
