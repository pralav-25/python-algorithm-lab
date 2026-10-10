import itertools
import unittest

from algorithm_lab.decode_ways import decode_ways


class Tests(unittest.TestCase):
    def test_all_digit_boundary_partitions(self):
        for size in range(6):
            for chars in itertools.product("0126", repeat=size):
                text = "".join(chars)
                expected = int(not text)
                if text:
                    for mask in range(1 << (size - 1)):
                        cuts = [0] + [i for i in range(1, size) if mask >> (i - 1) & 1] + [size]
                        chunks = [text[a:b] for a, b in zip(cuts, cuts[1:], strict=False)]
                        expected += all(
                            chunk[0] != "0" and 1 <= int(chunk) <= 26 for chunk in chunks
                        )
                self.assertEqual(decode_ways(text), expected)
        self.assertEqual(decode_ways("1111111111"), 89)

    def test_invalid_ascii_contract(self):
        for text in [None, True, b"12", "١٢", "１２", "1a", "1 2", "-1"]:
            with self.assertRaises(ValueError):
                decode_ways(text)
