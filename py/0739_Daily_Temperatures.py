import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        warmer_idx = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures) - 1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            if stack:
                warmer_idx[i] = stack[-1]
            stack.append(i)

        return [(w - i if w else 0) for i, w in enumerate(warmer_idx)]


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
