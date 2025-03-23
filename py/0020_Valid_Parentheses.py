import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) % 2:
            return False

        if s[0] not in ("(", "[", "{"):
            return False

        for c in s:
            if c in ("(", "[", "{"):
                stack.append(c)
            elif c == ")":
                if not stack or stack[-1] != "(":
                    return False
                stack.pop()
            elif c == "]":
                if not stack or stack[-1] != "[":
                    return False
                stack.pop()
            elif c == "}":
                if not stack or stack[-1] != "{":
                    return False
                stack.pop()

        return True if not stack else False


if __name__ == "__main__":
    solution = Solution()

    print(solution.isValid("()"))

    print(solution.isValid("()[]{}"))

    print(solution.isValid("(]"))

    print(solution.isValid("([])"))

    sys.exit(0)
