import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque

"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}

        def recursion(i):
            if i == 0:
                return 1

            if i in memo:
                return memo[i]

            ret = 1
            for j in range(0, i):
                if nums[i] > nums[j]:
                    ret = max(ret, recursion(j) + 1)
            memo[i] = ret

            return ret

        return max([recursion(i) for i in range(len(nums))])'
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        ret = 1

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

            ret = max(ret, dp[i])

        return ret


if __name__ == "__main__":
    solution = Solution()

    print(solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))

    print(solution.lengthOfLIS([0, 1, 0, 3, 2, 3]))

    print(solution.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))

    sys.exit(0)
