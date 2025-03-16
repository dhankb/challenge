import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class MedianFinder:

    def __init__(self):
        self.low = []
        self.high = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.low, -num)
        val = -heapq.heappop(self.low)
        heapq.heappush(self.high, val)

        if len(self.high) > len(self.low):
            val = heapq.heappop(self.high)
            heapq.heappush(self.low, -val)

    def findMedian(self) -> float:
        if len(self.high) == len(self.low):
            return (self.high[0] - self.low[0]) / 2.0
        else:
            return -self.low[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
