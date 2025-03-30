import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = nums[0]
        cur = 0

        while cur <= farthest and farthest < len(nums):
            farthest = max(farthest, cur + nums[cur])
            cur += 1

        return farthest >= len(nums) - 1


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
