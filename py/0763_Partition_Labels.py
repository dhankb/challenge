import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


"""
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        idx = {}
        pos = []
        for i, c in enumerate(s):
            if c in idx:
                pos[idx[c]][1] = i
            else:
                idx[c] = len(pos)
                pos.append([i, i])
        pos.sort()

        tmp = [pos[0]]
        for i in range(1, len(pos)):
            if pos[i][0] < tmp[-1][1]:
                tmp[-1][1] = max(tmp[-1][1], pos[i][1])
            else:
                tmp.append(pos[i][:])

        ret = []
        for e in tmp:
            ret.append(e[1] - e[0] + 1)

        return ret
"""


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_seen = {}
        for i, c in enumerate(s):
            last_seen[c] = i

        ret = []
        start, end = 0, 0
        for i, c in enumerate(s):
            end = max(end, last_seen[c])

            if i == end:
                ret.append(end - start + 1)
                start = i + 1

        return ret


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
