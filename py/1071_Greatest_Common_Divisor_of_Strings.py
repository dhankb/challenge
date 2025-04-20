import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(str1, str2):
            len1, len2 = len(str1), len(str2)
            mod_start = 0
            while str1 == str2[mod_start : mod_start + len1]:
                mod_start += len1

            if mod_start == 0:
                return ""
            elif mod_start == len2:
                return str1
            else:
                return gcd(str2[mod_start:], str1)

        if len(str1) <= len(str2):
            return gcd(str1, str2)
        else:
            return gcd(str2, str1)


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
