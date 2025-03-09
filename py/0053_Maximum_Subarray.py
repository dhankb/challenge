import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque

"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memo = {}

        def recursion(i):
            if i < 0:
                return 0

            if i in memo:
                return memo[i]

            ret = max(nums[i], nums[i] + recursion(i - 1))
            memo[i] = ret

            return ret

        return max([recursion(i) for i in range(len(nums))])
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums[:]
        ret = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i], dp[i] + dp[i - 1])
            ret = max(ret, dp[i])

        return ret


if __name__ == "__main__":
    solution = Solution()

    print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

    print(solution.maxSubArray([1]))

    print(solution.maxSubArray([5, 4, -1, 7, 8]))

    sys.exit(0)
