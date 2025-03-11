import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        max_freq = 0
        ret = None
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            if freq[num] > max_freq:
                max_freq = freq[num]
                ret = num

        return ret


if __name__ == "__main__":
    solution = Solution()

    print(solution.majorityElement([3, 2, 3]))

    print(solution.majorityElement([2, 2, 1, 1, 1, 2, 2]))

    sys.exit(0)
