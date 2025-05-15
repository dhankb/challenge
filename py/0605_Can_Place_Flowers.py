import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        while cnt < len(flowerbed) and n > 0:
            if not (
                flowerbed[cnt] == 1
                or (cnt - 1 >= 0 and flowerbed[cnt - 1] == 1)
                or (cnt + 1 < len(flowerbed) and flowerbed[cnt + 1] == 1)
            ):
                flowerbed[cnt] = 1
                n -= 1
            cnt += 1

        return n == 0


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
