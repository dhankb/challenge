import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class StockSpanner:

    def __init__(self):
        self.record = []

    def next(self, price: int) -> int:
        _span = 1

        while (idx := len(self.record) - _span) >= 0 and self.record[idx][0] <= price:
            _span += self.record[idx][1]

        self.record.append((price, _span))

        return _span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
