import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque

'''
class Solution:
    def partition(self, nums, start, end):
        l, r = start + 1, end
        while l <= r:
            while l <= r and nums[l] <= nums[start]:
                l += 1
            while l <= r and nums[r] >= nums[start]:
                r -= 1
            if l < r:
                nums[l], nums[r] = nums[r], nums[l]
        nums[start], nums[r] = nums[r], nums[start]
        return r

    def quick_sort(self, nums, start, end):
        if start < end:
            pivot = self.partition(nums, start, end)
            self.quick_sort(nums, start, pivot - 1)
            self.quick_sort(nums, pivot + 1, end)

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.quick_sort(nums, 0, len(nums) - 1)
'''


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        R, W, B = 0, 0, len(nums) - 1
        while W <= B:
            if nums[W] == 0:
                nums[R], nums[W] = nums[W], nums[R]
                R += 1
                W += 1
            elif nums[W] == 1:
                W += 1
            else:
                nums[W], nums[B] = nums[B], nums[W]
                B -= 1


if __name__ == "__main__":
    solution = Solution()

    nums = [2, 0, 2, 1, 1, 0]
    solution.sortColors(nums)
    print(nums)

    nums = [2, 0, 1]
    solution.sortColors(nums)
    print(nums)

    sys.exit(0)
