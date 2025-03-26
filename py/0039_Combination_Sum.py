import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []

        def backtracking(start, tmp, remain):
            if start >= len(candidates):
                return

            if remain == 0:
                ret.append(tmp[:])
                return

            for i in range(start, len(candidates)):
                if remain >= candidates[i]:
                    tmp.append(candidates[i])
                    backtracking(i, tmp, remain - candidates[i])
                    tmp.pop()

        backtracking(0, [], target)

        return ret


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
