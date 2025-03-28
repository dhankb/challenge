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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ret = ptr = prev_end = None
        cnt = 0

        while head:
            if cnt % 2 == 0:
                ptr = head
            else:
                ptr.next = head.next
                head.next = ptr
                if not ret:
                    ret = head
                else:
                    prev_end.next = head

                head = prev_end = ptr

            head = head.next
            cnt += 1

        return ret if ret else ptr


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
