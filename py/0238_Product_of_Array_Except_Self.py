import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [1] * len(nums)

        tmp = 1
        for i in range(len(nums)):
            ret[i] *= tmp
            tmp *= nums[i]

        tmp = 1
        for i in range(len(nums) - 1, -1, -1):
            ret[i] *= tmp
            tmp *= nums[i]

        return ret


if __name__ == "__main__":
    solution = Solution()

    print(solution.productExceptSelf([1, 2, 3, 4]))

    print(solution.productExceptSelf([-1, 1, 0, -3, 3]))

    sys.exit(0)
