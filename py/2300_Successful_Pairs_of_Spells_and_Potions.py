import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ret = []
        potions.sort()

        for spell in spells:
            l, r = 0, len(potions) - 1
            while l <= r:
                m = l + (r - l) // 2
                product = spell * potions[m]
                if product >= success:
                    r = m - 1
                elif product < success:
                    l = m + 1
            ret.append(len(potions) - l)

        return ret


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
