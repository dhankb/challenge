import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        fast = fast.next
        while slow.next != fast:
            node = slow.next
            slow.next = node.next
            node.next = fast.next
            fast.next = node

        ret = float("-inf")
        slow = slow.next
        while slow:
            ret = max(ret, head.val + slow.val)
            head = head.next
            slow = slow.next

        return ret
"""


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        record = []
        slow = fast = head
        while fast.next and fast.next.next:
            record.append(slow.val)
            fast = fast.next.next
            slow = slow.next
        record.append(slow.val)

        ret = float("-inf")
        slow = slow.next
        while record:
            ret = max(ret, slow.val + record.pop())
            slow = slow.next

        return ret


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
