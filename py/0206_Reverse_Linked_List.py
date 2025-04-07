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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = last = head
        while last and last.next:
            cur = last.next
            last.next = cur.next
            cur.next = head
            head = cur

        return head


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
