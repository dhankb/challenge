import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        kept = 1
        prev = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] >= intervals[prev][1]:
                prev = i
                kept += 1

        return len(intervals) - kept


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
