import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ret = 0

        def dfs(root, max_val):
            nonlocal ret

            if not root:
                return

            if root.val >= max_val:
                ret += 1
                max_val = root.val

            dfs(root.left, max_val)
            dfs(root.right, max_val)

        dfs(root, float("-inf"))
        return ret


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
