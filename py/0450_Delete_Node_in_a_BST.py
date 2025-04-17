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
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        orig_root = root
        parent = replace = None
        dir = 0

        while root and root.val != key:
            parent = root
            if root.val > key:
                root = root.left
                dir = -1
            elif root.val < key:
                root = root.right
                dir = 1

        if not root:
            return orig_root

        prev = None
        if root.right:
            replace = root.right
            while replace.left:
                prev = replace
                replace = replace.left
            if prev:
                prev.left = replace.right
                replace.right = root.right
            replace.left = root.left
        elif root.left:
            replace = root.left
            while replace.right:
                prev = replace
                replace = replace.right
            if prev:
                prev.right = replace.left
                replace.left = root.left
            replace.right = root.right

        if dir > 0:
            parent.right = replace
        elif dir < 0:
            parent.left = replace

        del root

        return (orig_root if parent else replace)


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
