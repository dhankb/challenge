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
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def recursion(start, end):
            if start > end:
                return None

            m = start + (end - start) // 2
            node = TreeNode(nums[m])
            node.left = recursion(start, m - 1)
            node.right = recursion(m + 1, end)

            return node

        return recursion(0, len(nums) - 1)


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
