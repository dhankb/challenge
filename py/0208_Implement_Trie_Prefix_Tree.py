import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Node:
    def __init__(self):
        self.isString = False
        self.next = [None] * 26


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if not cur.next[ord(c) - ord("a")]:
                cur.next[ord(c) - ord("a")] = Node()
            cur = cur.next[ord(c) - ord("a")]

        cur.isString = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if not cur.next[ord(c) - ord("a")]:
                return False
            cur = cur.next[ord(c) - ord("a")]

        return cur.isString

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if not cur.next[ord(c) - ord("a")]:
                return False
            cur = cur.next[ord(c) - ord("a")]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
