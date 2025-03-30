import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = [[1]]
        cnt = 1

        while cnt < numRows:
            tmp = [1]
            for i in range(1, len(ret[-1])):
                tmp.append(ret[-1][i] + ret[-1][i - 1])
            tmp.append(1)

            ret.append(tmp[:])
            cnt += 1

        return ret


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
