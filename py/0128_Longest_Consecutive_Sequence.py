import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        record = {}
        ret = 0
        for num in nums:
            greater = record.get(num + 1, 0)
            less = record.get(num - 1, 0)
            quantity = greater + less + 1
            record[num + greater] = record[num - less] = quantity
            ret = max(ret, quantity)

        return ret


if __name__ == "__main__":
    solution = Solution()

    print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))

    print(solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))

    sys.exit(0)
