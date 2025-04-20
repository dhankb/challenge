import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ret = [False] * len(candies)
        max_candy = None
        heap = []
        for i in range(len(candies)):
            heapq.heappush(heap, (-candies[i], i))
        max_candy = -heap[0][0]

        while heap:
            candy, i = heapq.heappop(heap)
            if -candy + extraCandies >= max_candy:
                ret[i] = True
            else:
                break

        return ret


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
