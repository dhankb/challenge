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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cnt = 0
        next_head = head
        while next_head and cnt < k:
            next_head = next_head.next
            cnt += 1

        if cnt != k:
            return head

        ptr = head
        head = self.reverseKGroup(next_head, k)
        cnt = 0
        while ptr and cnt < k:
            tmp = ptr.next
            ptr.next = head
            head = ptr
            ptr = tmp
            cnt += 1

        return head


if __name__ == "__main__":
    solution = Solution()

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head = solution.reverseKGroup(head, 2)
    while head:
        print(head.val)
        head = head.next

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head = solution.reverseKGroup(head, 3)
    while head:
        print(head.val)
        head = head.next

    sys.exit(0)
