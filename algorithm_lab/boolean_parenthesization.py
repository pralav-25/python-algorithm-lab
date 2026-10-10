"""Count false and true evaluations over all full parenthesizations.

The string must alternate literals T/F with binary operators &, | or ^, without
spaces. Empty input returns (0, 0). Return (false_count, true_count) as exact
integers. Every parenthesization is counted separately, so ties need no selection.
O(k cubed) time and O(k squared) space for k literals, excluding integer
arithmetic; the input is unchanged.

>>> boolean_parenthesization('T|F&T')
(0, 2)
>>> boolean_parenthesization('T^T|T')
(1, 1)
"""


def boolean_parenthesization(expression: str) -> tuple[int, int]:
    if not isinstance(expression, str):
        raise ValueError("expression must be a string")
    if not expression:
        return 0, 0
    if len(expression) % 2 != 1 or any(
        char not in ("TF" if index % 2 == 0 else "&|^") for index, char in enumerate(expression)
    ):
        raise ValueError("expression must alternate T/F literals and &, |, ^ operators")
    size = (len(expression) + 1) // 2
    counts = [[(0, 0) for _ in range(size)] for _ in range(size)]
    for index in range(size):
        counts[index][index] = (1, 0) if expression[2 * index] == "F" else (0, 1)
    for width in range(2, size + 1):
        for start in range(size - width + 1):
            end = start + width - 1
            false_count, true_count = 0, 0
            for split in range(start, end):
                operator = expression[2 * split + 1]
                for left, left_count in enumerate(counts[start][split]):
                    for right, right_count in enumerate(counts[split + 1][end]):
                        value = (
                            left & right
                            if operator == "&"
                            else left | right
                            if operator == "|"
                            else left ^ right
                        )
                        if value:
                            true_count += left_count * right_count
                        else:
                            false_count += left_count * right_count
            counts[start][end] = false_count, true_count
    return counts[0][-1]
