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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def builder(pre_start, pre_end, in_start, in_end):
            node = TreeNode(preorder[pre_start])
            idx = inorder.index(preorder[pre_start], in_start, in_end + 1)

            if idx != in_start:
                node.left = builder(pre_start + 1, pre_start + (idx - in_start), in_start, idx - 1)

            if idx != in_end:
                node.right = builder(pre_start + (idx - in_start) + 1, pre_end, idx + 1, in_end)

            return node

        if not preorder:
            return None

        return builder(0, len(preorder) - 1, 0, len(inorder) - 1)


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
