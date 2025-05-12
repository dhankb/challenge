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
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        fast = slow = head
        prev = None
        while fast.next and fast.next.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        if fast.next:
            prev = slow
            slow = slow.next
        prev.next = slow.next
        del slow

        return head


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
