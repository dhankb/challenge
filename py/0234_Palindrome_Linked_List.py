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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        if slow.next:
            h2 = last = slow.next
            slow.next = None

            while last.next:
                cur = last.next
                last.next = cur.next
                cur.next = h2
                h2 = cur

            while h2:
                if head.val != h2.val:
                    return False
                head = head.next
                h2 = h2.next

        return True


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
