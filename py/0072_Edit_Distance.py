import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def recursion(i, j):
            if i < 0 and j < 0:
                return 0
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1

            if (i, j) in memo:
                return memo[(i, j)]

            if word1[i] == word2[j]:
                memo[(i, j)] = recursion(i - 1, j - 1)
            else:
                memo[(i, j)] = min(recursion(i, j - 1), recursion(i - 1, j), recursion(i - 1, j - 1)) + 1

            return memo[(i, j)]

        return recursion(len(word1) - 1, len(word2) - 1)
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for i in range(len(word1) + 1):
            dp[i][0] = i

        for j in range(len(word2) + 1):
            dp[0][j] = j

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1

        return dp[len(word1)][len(word2)]


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
