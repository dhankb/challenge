import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = []
        memo = {}
        for s in strs:
            order_s = "".join(sorted(s))

            if order_s in memo:
                memo[order_s].append(s)
            else:
                memo[order_s] = [s]
                ret.append(memo[order_s])

        return ret


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
