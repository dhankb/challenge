import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ret = 0
        n = len(grid)

        def get_tuple(r, c):
            if r is not None:
                return tuple(grid[r])
            if c is not None:
                return tuple([grid[i][c] for i in range(n)])

        pool = {}
        for i in range(n):
            t = get_tuple(i, None)
            pool[t] = pool.get(t, 0) + 1

        for i in range(n):
            if (t := get_tuple(None, i)) in pool:
                ret += pool[t]

        return ret


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
