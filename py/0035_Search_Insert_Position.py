import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1

        return l


if __name__ == "__main__":
    solution = Solution()

    print(solution.searchInsert([1, 3, 5, 6], 5))

    print(solution.searchInsert([1, 3, 5, 6], 2))

    sys.exit(0)
