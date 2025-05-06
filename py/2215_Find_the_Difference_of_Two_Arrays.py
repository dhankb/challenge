import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        pool1 = set(nums1)
        pool2 = set(nums2)

        return [list(pool1 - pool2), list(pool2 - pool1)]


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
