import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ret = []
        letters = {
            "0": "",
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        if not digits:
            return ret

        def backtracking(i, tmp):
            if i == len(digits):
                ret.append("".join(tmp))
                return

            digit = digits[i]
            for l in letters[digit]:
                tmp.append(l)
                backtracking(i + 1, tmp)
                tmp.pop()

        backtracking(0, [])

        return ret


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
