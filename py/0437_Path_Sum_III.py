import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        total = []
        ret = 0

        def backtracking(root, total):
            nonlocal ret
            if not root:
                return

            total.append(0)
            for i in range(len(total)):
                total[i] += root.val
                if total[i] == targetSum:
                    ret += 1

            backtracking(root.left, total)
            backtracking(root.right, total)

            for i in range(len(total)):
                total[i] -= root.val
            total.pop()

        backtracking(root, total)
        return ret


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
