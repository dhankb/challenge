import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def bakctracking(i):
            if i <= 2:
                return i

            if i in memo:
                return memo[i]

            ret = 0
            for step in (1, 2):
                if i >= step:
                    ret += bakctracking(i - step)

            memo[i] = ret
            return memo[i]

        return bakctracking(n)


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
