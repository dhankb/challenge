import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        ret = 0
        first, last = [], []
        i, j = 0, len(costs) - 1

        for _ in range(k):
            while i <= j and len(first) < candidates:
                heapq.heappush(first, costs[i])
                i += 1

            while i <= j and len(last) < candidates:
                heapq.heappush(last, costs[j])
                j -= 1

            if first and last:
                if first[0] <= last[0]:
                    ret += heapq.heappop(first)
                else:
                    ret += heapq.heappop(last)
            elif first:
                ret += heapq.heappop(first)
            elif last:
                ret += heapq.heappop(last)
            else:
                break

        return ret


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
