import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


"""
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ret = float("inf")

        def dfs(x, y, steps):
            nonlocal ret
            if maze[x][y] != "X" and (x == 0 or x == len(maze) - 1 or y == 0 or y == len(maze[0]) - 1):
                ret = min(ret, steps)
                return

            for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                nx, ny = x + dx, y + dy
                if (
                    nx >= 0
                    and nx < len(maze)
                    and ny >= 0
                    and ny < len(maze[0])
                    and maze[nx][ny] != "+"
                    and maze[nx][ny] != "X"
                ):
                    maze[x][y] = "X"
                    dfs(nx, ny, steps + 1)
                    maze[x][y] = "."

        maze[entrance[0]][entrance[1]] = "X"
        dfs(entrance[0], entrance[1], 0)
        return -1 if ret == float("inf") else ret
"""


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        q = deque()
        q.append(entrance)
        steps = 0
        visited = set()
        visited.add((entrance[0], entrance[1]))

        while qsize := len(q):
            for _ in range(qsize):
                x, y = q.popleft()

                if (x == 0 or x == len(maze) - 1 or y == 0 or y == len(maze[0]) - 1) and steps != 0:
                    return steps

                for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < len(maze)
                        and 0 <= ny < len(maze[0])
                        and maze[nx][ny] != "+"
                        and (nx, ny) not in visited
                    ):
                        visited.add((nx, ny))
                        q.append((nx, ny))

            steps += 1

        return -1


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
