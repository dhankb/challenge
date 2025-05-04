import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


"""
class Solution:
    def numTilings(self, n: int) -> int:
        memo = {}

        def recursion(i):
            if i == 0:
                return 1

            if i in memo:
                return memo[i]

            tmp = 0
            for occupied in range(1, i + 1):
                possible = 1 if occupied <= 2 else 2
                tmp += recursion(i - occupied) * possible
                tmp %= 7 + 1000000000

            memo[i] = tmp
            return tmp

        return recursion(n)
"""


class Solution:
    def numTilings(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(n + 1):
            for occupied in range(1, i + 1):
                possible = 1 if occupied <= 2 else 2
                dp[i] += dp[i - occupied] * possible
                dp[i] %= 7 + 1000000000

        return dp[-1]


"""
dp[n]
= dp[n - 1] + dp[n - 2] + 2 * (dp[n - 3] + ... + d[0])
= dp[n - 1] + dp[n - 2] + dp[n - 3] + dp[n - 3] + 2 * (dp[n - 4] + ... + d[0])
= dp[n - 1] + dp[n - 3] + (dp[n - 2] + dp[n - 3] + 2 * (dp[n - 4]+ ... + d[0]))
= dp[n - 1] + dp[n - 3] + dp[n - 1]
= 2 * dp[n - 1] + dp[n - 3]
"""


class Solution:
    def numTilings(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = 2 * dp[i - 1] + dp[i - 3]
            dp[i] %= 7 + 1000000000


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
