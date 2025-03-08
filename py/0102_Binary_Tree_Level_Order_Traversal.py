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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []
        if not root: return ret

        q = deque()
        q.append(root)
        while (qsize := len(q)):
            level = []
            while qsize > 0:
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                level.append(node.val)
                qsize -= 1
            ret.append(level)
        return ret


if __name__ == "__main__":
    solution = Solution()

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(solution.levelOrder(root))

    root = TreeNode(1)
    print(solution.levelOrder(root))

    root = None
    print(solution.levelOrder(root))

    sys.exit(0)
