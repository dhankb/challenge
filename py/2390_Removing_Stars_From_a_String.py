import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for c in s:
            if c != "*":
                stack.append(c)
            elif stack:
                stack.pop()

        return "".join(stack)

if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
