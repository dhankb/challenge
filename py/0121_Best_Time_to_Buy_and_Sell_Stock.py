import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def recursion(buy, sell):
            if buy >= sell:
                return 0

            if (buy, sell) in memo:
                return memo[(buy, sell)]

            ret = max((0, prices[sell] - prices[buy], recursion(buy + 1, sell), recursion(buy, sell - 1)))
            memo[(buy, sell)] = ret

            return memo[(buy, sell)]

        return recursion(0, len(prices) - 1)
"""


"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * len(prices) for _ in range(len(prices))]

        for buy in range(len(prices) - 2, -1, -1):
            for sell in range(buy + 1, len(prices)):
                dp[buy][sell] = max(0, prices[sell] - prices[buy], dp[buy + 1][sell], dp[buy][sell - 1])

        return dp[0][len(prices) - 1]
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            lowest_price = min(lowest_price, prices[i])

            profit = max(profit, prices[i] - lowest_price)

        return profit


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
