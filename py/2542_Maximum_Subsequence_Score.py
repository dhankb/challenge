import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


"""
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ret = 0

        def backtracking(n, start, total, min_val):
            nonlocal ret
            if n > k:
                ret = max(ret, total * min_val)
                return

            if len(nums1) - start < k - n + 1:
                return

            for i in range(start, len(nums1) - k + n):
                backtracking(n + 1, i + 1, total + nums1[i], min_val if min_val <= nums2[i] else nums2[i])

        backtracking(1, 0, 0, float("inf"))
        return ret
"""


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ret = 0
        tmp = [(nums1[i], nums2[i]) for i in range(len(nums1))]
        tmp.sort(key=lambda e: (e[1], e[0]), reverse=True)
        min_heap = []
        nums1_total = 0

        for num1, num2 in tmp:
            nums1_total += num1
            heapq.heappush(min_heap, num1)

            if len(min_heap) == k:
                ret = max(ret, nums1_total * num2)
                nums1_total -= heapq.heappop(min_heap)

        return ret


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
