import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def recursion(i, j):
            if i < 0 or j < 0:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            if text1[i] == text2[j]:
                memo[(i, j)] = recursion(i - 1, j - 1) + 1
            else:
                memo[(i, j)] = max(recursion(i - 1, j), recursion(i, j - 1))

            return memo[(i, j)]

        return recursion(len(text1) - 1, len(text2) - 1)
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[len(text1)][len(text2)]


if __name__ == "__main__":
    solution = Solution()

    print(solution.longestCommonSubsequence("abcde", "ace"))

    print(solution.longestCommonSubsequence("abc", "abc"))

    print(solution.longestCommonSubsequence("abc", "def"))

    sys.exit(0)
