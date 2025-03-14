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


# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         if not root: return True
#         q = deque()
#         q.append(root)

#         while (qsize := len(q)):
#             level = deque()
#             for _ in range(qsize):
#                 node = q.popleft()
#                 if node:
#                     q.append(node.left)
#                     q.append(node.right)
#                     level.append(node.val)
#                 else:
#                      level.append(None)

#             while len(level) > 1:
#                 if level[0] != level[-1]:
#                     return False
#                 level.popleft()
#                 level.pop()

#         return True


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def recursion(r1, r2):
            if (not r1 and r2) or (r1 and not r2):
                return False

            if not r1 and not r1:
                return True

            if r1.val != r2.val:
                return False

            return recursion(r1.left, r2.right) and recursion(r1.right, r2.left)

        return recursion(root.left, root.right)


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
