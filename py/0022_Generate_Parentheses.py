import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []

        def backtracking(l, r, tmp):
            if r < l:
                return

            if l == 0 and r == 0:
                ret.append("".join(tmp))
                return

            if l:
                tmp.append("(")
                backtracking(l - 1, r, tmp)
                tmp.pop()

            if r:
                tmp.append(")")
                backtracking(l, r - 1, tmp)
                tmp.pop()

        backtracking(n, n, [])
        return ret


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
