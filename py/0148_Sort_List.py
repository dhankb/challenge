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
    def do_merge(self, h1, h2):
        header = ListNode()
        ptr = header

        while h1 and h2:
            if h1.val <= h2.val:
                ptr.next = h1
                h1 = h1.next
            else:
                ptr.next = h2
                h2 = h2.next
            ptr = ptr.next

        if h1:
            ptr.next = h1
        if h2:
            ptr.next = h2

        return header.next

    def merge_sort(self, h1, cnt):
        if cnt == 1:
            h1.next = None
            return h1
        else:
            half = cnt // 2
            tmp = 1
            h1_end = h1
            while tmp < half:
                h1_end = h1_end.next
                tmp += 1
            h2 = h1_end.next
            h1_end.next = None
            h1 = self.merge_sort(h1, half)
            h2 = self.merge_sort(h2, cnt - half)

            return self.do_merge(h1, h2)

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        ptr = head
        cnt = 0
        while ptr:
            cnt += 1
            ptr = ptr.next

        return self.merge_sort(head, cnt)


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
