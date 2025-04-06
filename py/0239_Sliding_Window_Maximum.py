import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class monotonic_queue:
    def __init__(self):
        self.q = deque()

    def push(self, num):
        while len(self.q) and self.q[-1] < num:
            self.q.pop()
        self.q.append(num)

    def pop(self, num):
        if len(self.q) and self.q[0] == num:
            self.q.popleft()

    def get_max(self):
        return self.q[0] if len(self.q) else None


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ret = []
        mq = monotonic_queue()
        for i in range(k):
            mq.push(nums[i])

        ret.append(mq.get_max())

        for i in range(k, len(nums)):
            mq.pop(nums[i - k])
            mq.push(nums[i])
            ret.append(mq.get_max())

        return ret


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
