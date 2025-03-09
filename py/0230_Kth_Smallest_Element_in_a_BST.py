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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ret = None

        def inorder(root, k):
            nonlocal ret
            if not root:
                return 0

            l_num = inorder(root.left, k)
            if k == l_num + 1:
                ret = root.val

            r_num = 0
            if k > l_num + 1:
                r_num = inorder(root.right, k - l_num - 1)

            return l_num + 1 + r_num

        inorder(root, k)
        return ret


if __name__ == "__main__":
    solution = Solution()

    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    print(solution.kthSmallest(root, 1))

    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)
    print(solution.kthSmallest(root, 3))

    sys.exit(0)
