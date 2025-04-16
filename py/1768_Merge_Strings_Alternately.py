import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ret = []
        i = 0

        while i < len(word1) and i < len(word2):
            ret.append(word1[i])
            ret.append(word2[i])
            i += 1

        if i < len(word1):
            ret.append(word1[i:])
        if i < len(word2):
            ret.append(word2[i:])

        return "".join(ret)


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
