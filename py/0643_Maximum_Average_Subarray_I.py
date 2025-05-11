import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[i] for i in range(k))
        ret = total
        start = 0

        while start < len(nums) - k:
            total = total - nums[start] + nums[start + k]
            ret = max(ret, total)
            start += 1

        return ret / k


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
