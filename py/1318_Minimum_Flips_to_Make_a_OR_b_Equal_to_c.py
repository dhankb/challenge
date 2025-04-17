import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ret = 0

        def to_bits(num):
            bits = []
            while num:
                bits.append(num % 2)
                num //= 2
            return bits

        a_bits = to_bits(a)
        b_bits = to_bits(b)
        c_bits = to_bits(c)

        max_len = max(len(a_bits), len(b_bits), len(c_bits))
        a_bits.extend([0] * (max_len - len(a_bits)))
        b_bits.extend([0] * (max_len - len(b_bits)))
        c_bits.extend([0] * (max_len - len(c_bits)))

        for i in range(len(c_bits)):
            if (a_bits[i] or b_bits[i]) != c_bits[i]:
                if c_bits[i]:
                    ret += 1
                else:
                    if a_bits[i]:
                        ret += 1
                    if b_bits[i]:
                        ret += 1
        return ret


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
