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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ret = []
        ret.extend(self.inorderTraversal(root.left))
        ret.append(root.val)
        ret.extend(self.inorderTraversal(root.right))

        return ret


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
