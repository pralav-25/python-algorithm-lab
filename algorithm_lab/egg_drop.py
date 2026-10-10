"""Return minimum worst-case drops needed to identify an egg-breaking floor.

Eggs must be a positive integer and floors a nonnegative integer; bool is
rejected. A broken egg cannot be reused. Zero floors needs zero drops. Only the
optimal count is returned, so tied strategies need no selection. For answer m
and e=min(eggs, floors), O(e*m) time and O(e) space excluding integer arithmetic;
no input mutation.

>>> egg_drop(2, 100)
14
>>> egg_drop(3, 14)
4
"""

from algorithm_lab._validation import integer


def egg_drop(eggs: int, floors: int) -> int:
    integer(eggs, "eggs", minimum=1)
    integer(floors, "floors", minimum=0)
    if not floors:
        return 0
    reachable = [0] * (min(eggs, floors) + 1)
    moves = 0
    while reachable[-1] < floors:
        moves += 1
        for count in range(len(reachable) - 1, 0, -1):
            reachable[count] = min(floors, reachable[count] + reachable[count - 1] + 1)
    return moves
