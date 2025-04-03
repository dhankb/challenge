import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ret = ""
        min_len = len(s) + 1
        need, record = {}, {}
        l, r = 0, 0
        valid = 0
        for c in t:
            need[c] = need.get(c, 0) + 1

        while r < len(s):
            new_char = s[r]
            r += 1

            if new_char in need:
                record[new_char] = record.get(new_char, 0) + 1
                if record[new_char] == need[new_char]:
                    valid += 1

            while valid == len(need):
                if r - l < min_len:
                    min_len = r - l
                    ret = s[l : r]

                del_char = s[l]
                l += 1

                if del_char in need:
                    record[del_char] -= 1
                    if record[del_char] < need[del_char]:
                        valid -= 1

        return "" if min_len == len(s) + 1 else ret


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
