import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        memo = {0: 1}
        ret = 0
        total = 0

        for num in nums:
            total += num

            if total - k in memo:
                ret += memo[total - k]

            memo[total] = memo.get(total, 0) + 1

        return ret


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
