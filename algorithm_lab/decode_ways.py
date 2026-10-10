"""Count decodings of ASCII digits into the symbols numbered 1 through 26.

The input must be a string containing only ASCII digits. A zero cannot decode
alone, and codes cannot have leading zeros. Empty text has one empty decoding.
Return an exact integer, counting all choices without tie selection. O(n) time
and O(1) auxiliary space excluding integer arithmetic; the input is unchanged.

>>> decode_ways('226')
3
>>> decode_ways('06')
0
"""


def decode_ways(text: str) -> int:
    if not isinstance(text, str) or any(char not in "0123456789" for char in text):
        raise ValueError("text must contain only ASCII digits")
    previous, current = 0, 1
    for index, char in enumerate(text):
        following = current if char != "0" else 0
        if index and "10" <= text[index - 1 : index + 1] <= "26":
            following += previous
        previous, current = current, following
    return current
