import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


"""
class Solution:
    def numSquares(self, n: int) -> int:
        memo = {}

        def backtracking(remain):
            sqrt = int(remain**0.5)
            if sqrt**2 == remain:
                return 1

            if remain in memo:
                return memo[remain]

            ret = float("inf")
            for i in range(sqrt, 0, -1):
                ret = min(ret, backtracking(remain - (i**2)) + 1)

            memo[remain] = ret
            return memo[remain]

        return backtracking(n)
"""


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            sqrt = int(i**0.5)
            for j in range(sqrt, 0, -1):
                dp[i] = min(dp[i], dp[i - j**2] + 1)

        return dp[n]


if __name__ == "__main__":
    solution = Solution()

    print(solution.numSquares(12))

    print(solution.numSquares(13))

    sys.exit(0)
