import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque

"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}

        def recursion(pos):
            if pos >= len(nums) - 1:
                return 0

            if pos in memo:
                return memo[pos]

            ret = float("inf")
            for jump in range(1, nums[pos] + 1):
                ret = min(ret, recursion(pos + jump) + 1)

            memo[pos] = ret
            return memo[pos]

        return recursion(0)
"""


"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float("inf")] * len(nums)
        dp[len(nums) - 1] = 0

        for pos in range(len(nums) - 2, -1, -1):
            for jump in range(1, nums[pos] + 1):
                if pos + jump < len(nums):
                    dp[pos] = min(dp[pos], dp[pos + jump] + 1)
                else:
                    break

        return dp[0]
"""


class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest, cur_farthest = 0, 0
        jumps = 0
        for pos in range(len(nums) - 1):
            farthest = max(farthest, pos + nums[pos])

            if pos == cur_farthest:
                jumps += 1
                cur_farthest = farthest

        return jumps


if __name__ == "__main__":
    solution = Solution()

    print(solution.jump([2, 3, 1, 1, 4]))

    print(solution.jump([2, 3, 0, 1, 4]))

    sys.exit(0)
