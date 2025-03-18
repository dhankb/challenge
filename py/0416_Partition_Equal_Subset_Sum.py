import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque

"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 == 1:
            return False
        target //= 2

        memo = {}

        def backtracking(i, goal):
            if goal == 0:
                return True

            if i == len(nums):
                return False

            if (i, goal) in memo:
                return memo[(i, goal)]

            ret = backtracking(i + 1, goal)
            if goal >= nums[i]:
                ret = ret or backtracking(i + 1, goal - nums[i])

            memo[(i, goal)] = ret
            return memo[(i, goal)]

        return backtracking(0, target)
"""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 == 1:
            return False
        target //= 2

        dp = [[False] * (target + 1) for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i][0] = True

        for i in range(len(nums)):
            for j in range(1, target + 1):
                if i - 1 >= 0:
                    dp[i][j] = dp[i - 1][j]
                if j >= nums[i]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j - nums[i]]

        return dp[len(nums) - 1][target]


if __name__ == "__main__":
    solution = Solution()

    print(solution.canPartition([1, 5, 11, 5]))

    print(solution.canPartition([1, 2, 3, 5]))

    print(solution.canPartition([1, 2, 5]))

    sys.exit(0)
