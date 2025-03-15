import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ret = []
        valid = 0
        need = {}
        window = {}

        for c in p:
            need[c] = need.get(c, 0) + 1

        l, r = 0, 0
        while r < len(s):
            c = s[r]
            r += 1

            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1

            while valid == len(need):
                if r - l == len(p):
                    ret.append(l)

                d = s[l]
                l += 1

                if d in need:
                    window[d] -= 1
                    if window[d] < need[d]:
                        valid -= 1
        return ret


if __name__ == "__main__":
    solution = Solution()

    print(solution.findAnagrams("cbaebabacd", "abc"))

    print(solution.findAnagrams("abab", "ab"))

    print(solution.findAnagrams("aabaa", "aa"))

    sys.exit(0)
