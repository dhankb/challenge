import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low, high = 1, len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2

            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1

            if cnt > mid:
                high = mid
            elif cnt <= mid:
                low = mid + 1

        return low


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
