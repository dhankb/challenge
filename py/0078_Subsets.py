import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []

        def backtracking(i, tmp):
            if i == len(nums):
                ret.append(tmp[:])
                return

            backtracking(i + 1, tmp)

            tmp.append(nums[i])
            backtracking(i + 1, tmp)
            tmp.pop()

        backtracking(0, [])
        return ret


if __name__ == "__main__":
    solution = Solution()

    print(solution.subsets([1, 2, 3]))

    print(solution.subsets([0]))

    sys.exit(0)
