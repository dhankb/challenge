import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        tmp, ret = 0, 0
        i = 0

        while i < len(s):
            if s[i] in ("a", "e", "i", "o", "u"):
                tmp += 1
            if i >= k and s[i - k] in ("a", "e", "i", "o", "u"):
                tmp -= 1
            ret = max(ret, tmp)
            i += 1

        return ret


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
