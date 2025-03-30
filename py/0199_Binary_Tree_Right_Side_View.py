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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        if not root:
            return ret
        q = deque()
        q.append(root)

        while q:
            ret.append(q[-1].val)
            qsize = len(q)
            for _ in range(qsize):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return ret


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
