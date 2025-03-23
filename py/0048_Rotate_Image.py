import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        start, end = 0, n - 1
        while start < end:
            for edge in range(start, end):
                ax, ay = start, edge
                bx, by = edge, n - 1 - start
                matrix[ax][ay], matrix[bx][by] = matrix[bx][by], matrix[ax][ay]
                cx, cy = n - 1 - start, n - 1 - edge
                matrix[ax][ay], matrix[cx][cy] = matrix[cx][cy], matrix[ax][ay]
                dx, dy = n - 1 - edge, start
                matrix[ax][ay], matrix[dx][dy] = matrix[dx][dy], matrix[ax][ay]

            start += 1
            end -= 1


if __name__ == "__main__":
    solution = Solution()

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solution.rotate(matrix)
    print(matrix)

    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    solution.rotate(matrix)
    print(matrix)

    sys.exit(0)
