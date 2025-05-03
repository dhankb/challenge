import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if t[j] == s[i]:
                i += 1
            j += 1

        return True if i == len(s) else False


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
