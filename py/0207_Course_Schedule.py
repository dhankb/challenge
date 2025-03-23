import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


"""
# Kahn's Algorithm (BFS)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        neighbors = {course: [] for course in range(numCourses)}
        in_degree = {course: 0 for course in range(numCourses)}

        for want, must in prerequisites:
            neighbors[want].append(must)
            in_degree[must] += 1

        count = 0
        q = deque()
        for course in range(numCourses):
            if in_degree[course] == 0:
                q.append(course)

        while q:
            course = q.popleft()
            count += 1
            for n in neighbors[course]:
                in_degree[n] -= 1
                if in_degree[n] == 0:
                    q.append(n)

        return count == numCourses
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        checked = set()
        path = []
        graph = [[] for _ in range(numCourses)]
        for want, must in prerequisites:
            graph[want].append(must)

        def has_cycle(course):
            if course in checked:
                return False

            if course in path:
                return True

            path.append(course)
            for n in graph[course]:
                if has_cycle(n):
                    return True
            path.pop()
            checked.add(course)

            return False

        for course in range(numCourses):
            if has_cycle(course):
                return False

        return True


if __name__ == "__main__":
    solution = Solution()

    print(solution.canFinish(2, [[1, 0]]))

    print(solution.canFinish(2, [[1, 0], [0, 1]]))

    sys.exit(0)
