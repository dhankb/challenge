import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max, current_min = 1, 1
        ret = nums[0]

        for num in nums:
            possibility = (num, num * current_max, num * current_min)
            current_max = max(possibility)
            current_min = min(possibility)
            ret = max(ret, current_max)

        return ret


if __name__ == "__main__":
    solution = Solution()

    print(solution.maxProduct([2, 3, -2, 4]))

    print(solution.maxProduct([-2, 0, -1]))

    sys.exit(0)
