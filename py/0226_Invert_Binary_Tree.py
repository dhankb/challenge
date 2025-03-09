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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root


if __name__ == "__main__":
    solution = Solution()

    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    root = solution.invertTree(root)
    print(root.val)
    print(root.left.val)
    print(root.right.val)
    print(root.left.left.val)
    print(root.left.right.val)
    print(root.right.left.val)
    print(root.right.right.val)

    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    root = solution.invertTree(root)
    print(root.val)
    print(root.left.val)
    print(root.right.val)

    root = solution.invertTree(None)
    print(root)

    sys.exit(0)
