import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ret = 0

        def dfs(x, y):
            grid[x][y] = "0"

            for sx, sy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                nx, ny = x + sx, y + sy
                if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[nx]) and grid[nx][ny] == "1":
                    dfs(nx, ny)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    ret += 1
                    dfs(i, j)

        return ret


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
