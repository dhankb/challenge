import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        i, j = 0, len(s) - 1
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

        while i < j:
            while s[i] not in vowels and i + 1 < len(s):
                i += 1
            while s[j] not in vowels and j - 1 >= 0:
                j -= 1

            if j < i:
                break

            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        return "".join(s)


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
