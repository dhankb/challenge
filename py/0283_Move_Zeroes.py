import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums

        non_zero = 0
        for num in nums:
            if num != 0:
                nums[non_zero] = num
                non_zero += 1

        for i in range(non_zero, len(nums)):
            nums[i] = 0


if __name__ == "__main__":
    solution = Solution()

    nums = [0, 1, 0, 3, 12]
    solution.moveZeroes(nums)
    print(nums)

    nums = [0]
    solution.moveZeroes(nums)
    print(nums)

    sys.exit(0)
