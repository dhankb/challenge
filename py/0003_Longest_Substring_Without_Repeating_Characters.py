import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        l, r = 0, 0
        ret = 0

        while r < len(s):
            ch = s[r]
            window[ch] = window.get(ch, 0) + 1

            while window[ch] > 1:
                ch_del = s[l]
                l += 1

                window[ch_del] -= 1

            r += 1
            ret = max(ret, r - l)

        return ret


if __name__ == "__main__":
    solution = Solution()

    print(solution.lengthOfLongestSubstring("abcabcbb"))

    print(solution.lengthOfLongestSubstring("bbbbb"))

    print(solution.lengthOfLongestSubstring("pwwkew"))

    print(solution.lengthOfLongestSubstring(" "))

    sys.exit(0)
