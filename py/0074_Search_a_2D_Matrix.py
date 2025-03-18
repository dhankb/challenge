import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        def get_value(mid):
            return matrix[mid // n][mid % n]

        l, r = 0, (m * n - 1)
        while l <= r:
            mid = l + (r - l) // 2
            val = get_value(mid)
            if val == target:
                return True
            elif val > target:
                r = mid - 1
            else:
                l = mid + 1

        return False


if __name__ == "__main__":
    solution = Solution()

    print(solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))

    print(solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))

    sys.exit(0)
