import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def bakctracking(start):
            if start == len(s):
                return True

            if start in memo:
                return memo[start]

            ret = False
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordDict and bakctracking(end):
                    ret = ret or True

            memo[start] = ret
            return memo[start]

        return bakctracking(0)
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for end in range(1, len(s) + 1):
            for start in range(end):
                if s[start:end] in wordDict and dp[start]:
                    dp[end] = True

        return dp[len(s)]


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
