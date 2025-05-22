import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1

        dp = [0] * (n + 1)
        dp[1] = dp[2] = 1

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        return dp[-1]

if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
