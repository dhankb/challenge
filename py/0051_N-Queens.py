import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def attack(self, board, n, i, j):
        for row in board:
            if row[j] == "Q":
                return True

        l, r = j, j
        for ni in range(i - 1, -1, -1):
            l -= 1
            r += 1
            if l >= 0 and board[ni][l] == "Q":
                return True
            if r < n and board[ni][r] == "Q":
                return True

        return False

    def solveNQueens(self, n: int) -> List[List[str]]:
        ret = []

        def recursion(i, board):
            if i == n:
                ret.append(board[:])
                return

            for j in range(n):
                if not self.attack(board, n, i, j):
                    board.append("." * j + "Q" + "." * (n - j - 1))
                    recursion(i + 1, board)
                    board.pop()

        recursion(0, [])
        return ret


if __name__ == "__main__":
    solution = Solution()

    print(solution.solveNQueens(1))

    print(solution.solveNQueens(4))

    sys.exit(0)
