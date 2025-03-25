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


"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited = set()
        while headA:
            visited.add(headA)
            headA = headA.next

        while headB:
            if headB in visited:
                return headB
            headB = headB.next

        return None
"""


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA = lenB = 0
        lastA = lastB = None

        ptr = headA
        while ptr:
            lenA += 1
            lastA = ptr
            ptr = ptr.next

        ptr = headB
        while ptr:
            lenB += 1
            lastB = ptr
            ptr = ptr.next

        if lastA != lastB:
            return None

        if lenA > lenB:
            for _ in range(lenA - lenB):
                headA = headA.next
        elif lenA < lenB:
            for _ in range(lenB - lenA):
                headB = headB.next

        while headA != headB:
            headA = headA.next
            headB = headB.next

        return headA


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
