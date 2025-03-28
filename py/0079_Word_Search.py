import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x, y, idx):
            if idx == len(word):
                return True

            for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                nx, ny = x + dx, y + dy
                if nx >= 0 and nx < len(board) and ny >= 0 and ny < len(board[nx]) and board[nx][ny] == word[idx]:
                    c, board[nx][ny] = board[nx][ny], "."
                    ret = dfs(nx, ny, idx + 1)
                    board[nx][ny] = c
                    if ret:
                        return True

            return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    c, board[i][j] = board[i][j], "."
                    ret = dfs(i, j, 1)
                    board[i][j] = c

                    if ret:
                        return True

        return False


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
