import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}

        for i, num in enumerate(nums):
            if target - num in memo:
                return [memo[target - num], i]
            memo[num] = i

        return [-1, -1]


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
