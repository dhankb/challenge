import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            print(l, r)
            m = l + (r - l) // 2

            if nums[m] == target:
                return m

            if nums[l] <= nums[r]:
                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
            else:
                if nums[m] > target:
                    if nums[m] >= nums[l]:
                        if target >= nums[l]:
                            r = m - 1
                        else:
                            l = m + 1
                    else:
                        r = m - 1
                elif nums[m] < target:
                    if nums[m] <= nums[r]:
                        if target <= nums[r]:
                            l = m + 1
                        else:
                            r = m -1
                    else:
                        l = m + 1

        return -1


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
