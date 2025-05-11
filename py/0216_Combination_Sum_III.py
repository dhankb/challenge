import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n < sum(i for i in range(1, k + 1)) or n > sum(i for i in range(9, 9 - k, -1)):
            return []

        ret = []

        def backtracking(k, start, target, tmp):
            if k == 0:
                if target == 0:
                    ret.append(tmp[:])
                return

            if start > 9:
                return

            for num in range(start, 10 - k + 1):
                if num > target:
                    break

                tmp.append(num)
                backtracking(k - 1, num + 1, target - num, tmp)
                tmp.pop()

        backtracking(k, 1, n, [])

        return ret


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
