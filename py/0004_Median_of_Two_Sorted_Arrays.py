import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        total_len = m + n
        smaller_size = (total_len + 1) // 2
        low, high = 0, m

        while low <= high:
            mid1 = low + (high - low) // 2
            mid2 = smaller_size - mid1

            L1, L2 = float("-inf"), float("-inf")
            R1, R2 = float("inf"), float("inf")
            if mid1 < m:
                R1 = nums1[mid1]
            if mid2 < n:
                R2 = nums2[mid2]
            if mid1 - 1 >= 0:
                L1 = nums1[mid1 - 1]
            if mid2 - 1 >= 0:
                L2 = nums2[mid2 - 1]

            if L1 <= R2 and L2 <= R1:
                if total_len % 2 == 1:
                    return max(L1, L2)
                else:
                    return (max(L1, L2) + min(R1, R2)) / 2.0
            elif L1 > R2:
                high = mid1 - 1
            elif L2 > R1:
                low = mid1 + 1

        return -1


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
