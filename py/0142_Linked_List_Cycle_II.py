import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        if not fast.next or not fast.next.next:
            return None

        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next

        return slow


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
