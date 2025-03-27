import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ret = []

        for interval in intervals:
            if ret and interval[0] <= ret[-1][1]:
                ret[-1][1] = max(ret[-1][1], interval[1])
            else:
                ret.append(interval[:])

        return ret


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
