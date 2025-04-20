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
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaf_val(root):
            if not root:
                return []

            ltree = get_leaf_val(root.left)
            rtree = get_leaf_val(root.right)

            if not ltree and not rtree:
                return [root.val]

            return ltree + rtree

        return get_leaf_val(root1) == get_leaf_val(root2)


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
