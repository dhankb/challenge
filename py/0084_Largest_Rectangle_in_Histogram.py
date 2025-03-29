import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ret = 0

        heights.append(0)
        for i, height in enumerate(heights):
            while stack and stack[-1][1] >= height:
                _, H = stack.pop()
                W_start = stack[-1][0] if stack else -1
                W = i - W_start - 1
                ret = max(ret, H * W)
            stack.append((i, height))

        return ret


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
