import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Solution:
    def compress(self, chars: List[str]) -> int:
        ret, i = 0, 0
        while i < len(chars):
            cnt = 1
            while i + cnt < len(chars) and chars[i + cnt] == chars[i]:
                cnt += 1

            chars[ret] = chars[i]
            ret += 1
            if cnt > 1:
                for c in str(cnt):
                    chars[ret] = c
                    ret += 1

            i += cnt

        return ret


if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
