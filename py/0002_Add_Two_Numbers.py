import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        header = ListNode()
        cur = header
        carry_on = False
        while l1 or l2:
            val = 0
            if l1:
                val += l1.val
            if l2:
                val += l2.val
            if carry_on:
                val += 1

            if val > 9:
                val -= 10
                carry_on = True
            else:
                carry_on = False

            cur.next = ListNode(val)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry_on:
            cur.next = ListNode(1)

        return header.next


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
