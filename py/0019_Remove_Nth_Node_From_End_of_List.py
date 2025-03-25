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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head

        for _ in range(n):
            fast = fast.next

        prev = None
        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next

        if prev:
            prev.next = slow.next
            del slow
        else:
            prev = head
            head = head.next
            del prev

        return head


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
