import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ret = []

        def is_palindrome(l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtracking(start, tmp):
            if start == len(s):
                ret.append(tmp[:])
                return

            for end in range(start + 1, len(s) + 1):
                if is_palindrome(start, end - 1):
                    tmp.append(s[start:end])
                    backtracking(end, tmp)
                    tmp.pop()

        backtracking(0, [])

        return ret


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
