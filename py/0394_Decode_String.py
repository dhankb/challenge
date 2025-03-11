import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


# class Solution:
#     def decodeString(self, s: str) -> str:
#         cur_times = 0
#         cur_buf = ""
#         stack = []

#         for c in s:
#             if c == "[":
#                 stack.append((cur_buf, cur_times))
#                 cur_buf = ""
#                 cur_times = 0
#             elif c == "]":
#                 prev_buf, prev_times = stack.pop()
#                 cur_buf = prev_buf + prev_times * cur_buf
#             elif c.isdigit():
#                 cur_times = cur_times * 10 + int(c)
#             elif c.isalpha():
#                 cur_buf += c

#         return cur_buf


class Solution:
    def decodeString(self, s: str) -> str:
        i = 0

        def recursion():
            nonlocal i
            buf = ""
            times = 0
            while i < len(s):
                if s[i] == "[":
                    i += 1
                    buf += times * recursion()
                    times = 0
                elif s[i] == "]":
                    return buf
                elif s[i].isdigit():
                    times = times * 10 + int(s[i])
                elif s[i].isalpha():
                    buf += s[i]
                i += 1

            return buf

        return recursion()


if __name__ == "__main__":
    solution = Solution()

    print(solution.decodeString("3[a]2[bc]"))

    print(solution.decodeString("3[a2[c]]"))

    print(solution.decodeString("2[abc]3[cd]ef"))

    print(solution.decodeString("5[c2[a3[d]]]4[x]"))

    print(solution.decodeString("2[y]pq4[2[jk]e]"))

    print(solution.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))

    sys.exit(0)
