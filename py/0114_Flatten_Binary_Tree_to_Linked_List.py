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


'''
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        ltree, rtree = root.left, root.right

        self.flatten(ltree)
        self.flatten(rtree)

        if ltree:
            root.left = None
            root.right = ltree

            if rtree:
                ptr = root
                while ptr.right:
                    ptr = ptr.right
                ptr.right = rtree
'''


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while root:
            if root.left:
                ptr = root.left
                while ptr.right:
                    ptr = ptr.right
                ptr.right = root.right
                root.right = root.left
                root.left = None
            root = root.right


if __name__ == "__main__":
    solution = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)

    solution.flatten(root)
    while root:
        print(root, root.val)
        if root.left:
            print("error")
        root = root.right

    sys.exit(0)
