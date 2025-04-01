import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = [[False] * len(matrix[i]) for i in range(len(matrix))]
        shift = ((0, 1), (1, 0), (0, -1), (-1, 0))
        ret = []

        def dfs(x, y, dir):
            visited[x][y] = True
            ret.append(matrix[x][y])

            nx, ny = x + shift[dir][0], y + shift[dir][1]
            if nx >= 0 and nx < len(matrix) and ny >= 0 and ny < len(matrix[nx]) and not visited[nx][ny]:
                dfs(nx, ny, dir)
            else:
                dir = (dir + 1) % 4
                nx, ny = x + shift[dir][0], y + shift[dir][1]
                if nx >= 0 and nx < len(matrix) and ny >= 0 and ny < len(matrix[nx]) and not visited[nx][ny]:
                    dfs(nx, ny, dir)

        dfs(0, 0, 0)

        return ret


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
