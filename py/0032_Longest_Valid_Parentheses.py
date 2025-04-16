import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ret = 0
        stack = [-1]

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    ret = max(ret, i - stack[-1])
                else:
                    stack.append(i)

        return ret


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
