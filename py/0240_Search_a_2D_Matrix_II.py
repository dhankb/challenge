import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        if target > matrix[m - 1][n - 1]:
            return False

        visited = [[False] * n for _ in range(m)]

        anchor = 0
        while anchor < min(m, n):
            if target == matrix[anchor][anchor]:
                return True
            elif target > matrix[anchor][anchor]:
                visited[anchor][anchor] = True
            else:
                for i in range(anchor - 1):
                    visited[i][anchor - 1] = True
                    visited[anchor - 1][i] = True
                break

            anchor += 1

        q = deque()
        q.append((anchor - 1, anchor - 1))
        while q:
            x, y = q.pop()
            visited[x][y] = True

            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                shift = ((0, 1), (1, 0))
            else:
                shift = ((0, -1), (-1, 0))

            for sx, sy in shift:
                nx, ny = x + sx, y + sy
                if nx >= 0 and nx < m and ny >= 0 and ny < n and not visited[nx][ny]:
                    q.append((nx, ny))

        return False
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        if target > matrix[m - 1][n - 1]:
            return False

        i, j = m - 1, 0
        while i >= 0 and j < n:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j += 1
            else:
                i -= 1

        return False


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
