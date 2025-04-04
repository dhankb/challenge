import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ret = []
        heap = []
        record = {}

        for num in nums:
            record[num] = record.get(num, 0) + 1

        for num, times in record.items():
            heapq.heappush(heap, (-times, num))

        for _ in range(k):
            _, num = heapq.heappop(heap)
            ret.append(num)

        return ret


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
