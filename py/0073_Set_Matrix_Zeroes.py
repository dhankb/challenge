import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return

        m, n = len(matrix), len(matrix[0])
        zero_row = True if matrix[0][0] == 0 else False
        zero_col = True if matrix[0][0] == 0 else False
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0:
                        zero_row = True
                    elif j == 0:
                        zero_col = True
                    else:
                        matrix[i][0] = 0
                        matrix[0][j] = 0

        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        if zero_col:
            for i in range(m):
                matrix[i][0] = 0

        if zero_row:
            for j in range(n):
                matrix[0][j] = 0


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
