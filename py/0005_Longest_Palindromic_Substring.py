import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        ret = s[0]
        dp = [[False] * len(s) for _ in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = True

        for l in range(len(s) - 1, -1, -1):
            for r in range(l + 1, len(s)):
                if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
                    dp[l][r] = True

                    if r - l + 1 > len(ret):
                        ret = s[l : r + 1]

        return ret


if __name__ == "__main__":
    solution = Solution()

    print(solution.longestPalindrome("babad"))

    print(solution.longestPalindrome("cbbd"))

    sys.exit(0)
