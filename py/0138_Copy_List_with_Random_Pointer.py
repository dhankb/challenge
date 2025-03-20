import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return head

        node_mapping = {head: Node(head.val)}
        ret = node_mapping[head]

        orig_ptr = head.next
        new_ptr = ret
        while orig_ptr:
            node_mapping[orig_ptr] = Node(orig_ptr.val)
            new_ptr.next = node_mapping[orig_ptr]
            new_ptr = new_ptr.next
            orig_ptr = orig_ptr.next

        orig_ptr = head
        new_ptr = ret
        while orig_ptr:
            new_ptr.random = None if not orig_ptr.random else node_mapping[orig_ptr.random]
            new_ptr = new_ptr.next
            orig_ptr = orig_ptr.next

        return ret


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
