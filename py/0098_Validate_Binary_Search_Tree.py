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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recursion(root, max_val, min_val):
            if not root:
                return True

            if root.val >= max_val:
                return False
            if root.val <= min_val:
                return False

            return recursion(root.left, root.val, min_val) and recursion(root.right, max_val, root.val)

        return recursion(root, float("inf"), float("-inf"))


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
