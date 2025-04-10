import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ret = 0
        for num in nums:
            ret ^= num

        return ret


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
