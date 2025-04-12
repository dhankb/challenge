import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(start, target):
            tmp = []
            l, r = start, len(nums) - 1
            while l < r:
                val = nums[l] + nums[r]
                if val > target:
                    while r - 1 > l and nums[r - 1] == nums[r]:
                        r -= 1
                    r -= 1
                elif val < target:
                    while l + 1 < r and nums[l + 1] == nums[l]:
                        l += 1
                    l += 1
                else:
                    tmp.append([nums[l], nums[r]])
                    while r - 1 > l and nums[r - 1] == nums[r]:
                        r -= 1
                    r -= 1
                    while l + 1 < r and nums[l + 1] == nums[l]:
                        l += 1
                    l += 1
            return tmp

        ret = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if remain := twoSum(i + 1, -nums[i]):
                for tmp in remain:
                    ret.append([nums[i], tmp[0], tmp[1]])

        return ret


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
