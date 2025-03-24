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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def merge(l1, l2):
            head = ListNode()
            ptr = head

            while l1 and l2:
                if l1.val <= l2.val:
                    ptr.next = l1
                    l1 = l1.next
                else:
                    ptr.next = l2
                    l2 = l2.next
                ptr = ptr.next

            if l1:
                ptr.next = l1

            if l2:
                ptr.next = l2

            return head.next

        while len(lists) > 1:
            tmp = []
            for i in range(0, len(lists), 2):
                tmp.append(merge(lists[i], lists[i + 1] if i + 1 < len(lists) else None))
            lists = tmp

        return lists[0]


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
