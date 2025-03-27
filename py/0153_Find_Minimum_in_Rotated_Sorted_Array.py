import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2
            if nums[l] > nums[r]:
                if nums[m] >= nums[l]:
                    l = m + 1
                elif nums[m] < nums[l]:
                    r = m
            else:
                r = m - 1

        return nums[l]


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
