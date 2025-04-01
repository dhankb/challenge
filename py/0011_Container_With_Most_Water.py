import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ret = 0

        while l < r:
            ret = max(ret, (r - l) * min(height[l], height[r]))
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return ret


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
