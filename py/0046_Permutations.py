import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        visited = [False] * len(nums)
        def backtracking(tmp):
            if len(tmp) == len(nums):
                ret.append(tmp[:])

            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    tmp.append(nums[i])
                    backtracking(tmp)
                    tmp.pop()
                    visited[i] = False

        backtracking([])
        return ret

if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
