import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def recursion(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])

            if i in memo:
                return memo[i]

            memo[i] = max(recursion(i - 2) + nums[i], recursion(i - 1))
            return memo[i]

        return recursion(len(nums) - 1)
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = nums[:]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
