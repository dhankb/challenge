import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        memo = {}
        ret = 0

        for num in nums:
            if k - num in memo and memo[k - num]:
                memo[k - num] -= 1
                ret += 1
            else:
                memo[num] = memo.get(num, 0) + 1

        return ret


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
