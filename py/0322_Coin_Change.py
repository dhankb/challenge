import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def backtracking(remain):
            if remain == 0:
                return 0

            if remain in memo:
                return memo[remain]

            ret = remain + 1
            for c in coins:
                if c <= remain and (tmp := backtracking(remain - c)) != -1:
                    ret = min(ret, tmp + 1)

            memo[remain] = (-1 if ret == remain + 1 else ret)
            return memo[remain]

        return backtracking(amount)
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for n in range(1, amount + 1):
            for c in coins:
                if c <= n:
                    dp[n] = min(dp[n], dp[n - c] + 1)

        return -1 if dp[amount] == float("inf") else dp[amount]


if __name__ == "__main__":
    solution = Solution()

    print(solution.coinChange([1, 2, 5], 11))

    print(solution.coinChange([2], 3))

    print(solution.coinChange([1], 0))

    sys.exit(0)
