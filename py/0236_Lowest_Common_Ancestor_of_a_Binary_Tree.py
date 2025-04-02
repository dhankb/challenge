import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        if not root:
            return None

        is_root = False
        if p == root or q == root:
            return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root
        elif l:
            return root.left
        elif r:
            return root.right
        else:
            return None


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
