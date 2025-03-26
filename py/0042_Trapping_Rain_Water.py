import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


"""
class Solution:
    def trap(self, height: List[int]) -> int:
        lh = []
        rh = []
        ret = 0

        tmp_max = -1
        for i in range(len(height)):
            tmp_max = max(tmp_max, height[i])
            lh.append(tmp_max)

        tmp_max = -1
        for i in range(len(height) - 1, -1, -1):
            tmp_max = max(tmp_max, height[i])
            rh.insert(0, tmp_max)

        for i in range(len(height)):
            if lh[i] != -1 and rh[i] != -1:
                ret += min(lh[i], rh[i]) - height[i]

        return ret
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lmax, rmax = height[l], height[r]
        ret = 0

        while l < r:
            if lmax < rmax:
                ret += lmax - height[l]
                l += 1
                lmax = max(lmax, height[l])
            else:
                ret += rmax - height[r]
                r -= 1
                rmax = max(rmax, height[r])

        return ret


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
