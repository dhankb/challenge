import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


"""
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        rc, dc = 0, 0
        for i in range(len(senate) - 1, -1, -1):
            if senate[i] == "R":
                rc += 1
            elif senate[i] == "D":
                dc += 1

        i = 0
        while rc != 0 and dc != 0:
            if senate[i] == "R":
                dc -= 1
                if dc:
                    lose = i
                    while senate[lose] != "D":
                        lose = (lose + 1) % len(senate)
                    senate[lose] = "."
            elif senate[i] == "D":
                rc -= 1
                if rc:
                    lose = i
                    while senate[lose] != "R":
                        lose = (lose + 1) % len(senate)
                    senate[lose] = "."
            i = (i + 1) % len(senate)

        return "Radiant" if dc == 0 else "Dire"
"""


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rq, dq = deque(), deque()
        for i in range(len(senate)):
            queue = rq if senate[i] == "R" else dq
            queue.append(i)

        i = len(senate)
        while rq and dq:
            r = rq.popleft()
            d = dq.popleft()
            queue = rq if r < d else dq
            queue.append(i)
            i += 1

        return "Radiant" if len(dq) == 0 else "Dire"


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
