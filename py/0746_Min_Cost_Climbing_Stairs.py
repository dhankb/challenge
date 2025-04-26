import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)

        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])

        return dp[-1]


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
