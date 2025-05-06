import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        memo = {}
        for num in arr:
            memo[num] = memo.get(num, 0) + 1

        visited = set()
        for _, times in memo.items():
            if times in visited:
                return False
            visited.add(times)
        return True


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
