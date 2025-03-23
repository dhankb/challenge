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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ret = 0

        def recursion(root):
            nonlocal ret
            if not root:
                return 0

            l, r = recursion(root.left), recursion(root.right)

            ret = max(ret, l + r)

            return max(l, r) + 1

        recursion(root)
        return ret


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
