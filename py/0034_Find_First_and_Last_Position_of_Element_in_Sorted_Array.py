import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ret = []

        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] >= target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1

        if l > len(nums) - 1 or nums[l] != target:
            return [-1, -1]
        else:
            ret.append(l)

        l, r = l, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] <= target:
                l = m + 1

        if r < 0 or nums[r] != target:
            return [-1, -1]
        else:
            ret.append(r)

        return ret


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
