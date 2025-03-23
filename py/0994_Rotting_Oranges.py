import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ret = -1
        have_fresh = False
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    have_fresh = True

        if not q:
            return -1 if have_fresh else 0

        while qsize := len(q):
            ret += 1
            for _ in range(qsize):
                x, y = q.popleft()

                for sx, sy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                    nx, ny = x + sx, y + sy
                    if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]) or grid[nx][ny] != 1:
                        continue

                    grid[nx][ny] = 2
                    q.append((nx, ny))

        for raw in grid:
            for cell in raw:
                if cell == 1:
                    return -1

        return ret


if __name__ == "__main__":
    solution = Solution()

    print(solution.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))

    print(solution.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))

    print(solution.orangesRotting([[0, 2]]))

    sys.exit(0)
