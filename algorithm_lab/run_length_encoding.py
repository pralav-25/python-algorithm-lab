"""Encode consecutive Unicode code points as (character, count) runs.

Encoding takes O(n) time and O(r) output space. Decoding takes O(output length)
time and space, and refuses output exceeding max_output before allocating it.
Counts must be positive integers, and symbols must be single code points.

>>> encode_runs('aa🙂🙂b')
[('a', 2), ('🙂', 2), ('b', 1)]
>>> decode_runs([('x', 3)])
'xxx'
"""

from collections.abc import Iterable


def encode_runs(text: str) -> list[tuple[str, int]]:
    result = []
    for char in text:
        if result and result[-1][0] == char:
            result[-1] = (char, result[-1][1] + 1)
        else:
            result.append((char, 1))
    return result


def decode_runs(runs: Iterable[tuple[str, int]], *, max_output: int = 1_000_000) -> str:
    if isinstance(max_output, bool) or not isinstance(max_output, int) or max_output < 0:
        raise ValueError("max_output must be a nonnegative integer")
    parts, length = [], 0
    for char, count in runs:
        if not isinstance(char, str) or len(char) != 1:
            raise ValueError("each symbol must be one code point")
        if isinstance(count, bool) or not isinstance(count, int) or count < 1:
            raise ValueError("counts must be positive integers")
        length += count
        if length > max_output:
            raise ValueError("decoded text exceeds max_output")
        parts.append(char * count)
    return "".join(parts)
