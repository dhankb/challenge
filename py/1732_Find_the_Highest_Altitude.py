import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        height = 0
        ret = 0
        for g in gain:
            height += g
            ret = max(ret, height)

        return ret


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
