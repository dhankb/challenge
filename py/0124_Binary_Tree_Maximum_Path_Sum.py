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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ret = float("-inf")

        def recursion(head):
            nonlocal ret
            if not head:
                return 0

            val = head.val
            print(val, ret)
            lvalue = recursion(head.left)
            rvalue = recursion(head.right)

            if lvalue > 0 and rvalue > 0:
                ret = max(ret, val + lvalue + rvalue)
                return val + max(lvalue, rvalue)
            elif lvalue > 0:
                ret = max(ret, val + lvalue)
                return val + lvalue
            elif rvalue > 0:
                ret = max(ret, val + rvalue)
                return val + rvalue
            else:
                ret = max(ret, val)
                return val

        recursion(root)
        return ret


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
