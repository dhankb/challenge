import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            m = l + (r - l) // 2
            eat_hours = sum([math.ceil(p / m) for p in piles])
            print(f"{m}: {eat_hours}")
            if eat_hours > h:
                l = m + 1
            elif eat_hours <= h:
                r = m - 1

        return l


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
