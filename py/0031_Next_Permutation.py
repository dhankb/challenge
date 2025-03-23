import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse_in_place(start):
            end = len(nums) - 1
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        target = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                target = i - 1
                break

        if target != -1:
            i = len(nums) - 1
            while nums[i] <= nums[target]:
                i -= 1
            nums[target], nums[i] = nums[i], nums[target]

        reverse_in_place(target + 1)


if __name__ == "__main__":
    solution = Solution()

    nums = [1, 2, 3]
    solution.nextPermutation(nums)
    print(nums)

    nums = [3, 2, 1]
    solution.nextPermutation(nums)
    print(nums)

    nums = [1, 1, 5]
    solution.nextPermutation(nums)
    print(nums)

    sys.exit(0)
