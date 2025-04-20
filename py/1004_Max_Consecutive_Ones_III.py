import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ret = k
        cnt = 0
        l, r = 0, 0
        while r < len(nums):
            c = nums[r]
            r += 1
            if c == 0:
                cnt += 1

            while cnt > k:
                ret = max(ret, r - l - 1)

                c = nums[l]
                l += 1
                if c == 0:
                    cnt -= 1

        return max(ret, r - l)


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
