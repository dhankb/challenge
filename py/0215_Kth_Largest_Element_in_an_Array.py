import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        return nums[-k]


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
