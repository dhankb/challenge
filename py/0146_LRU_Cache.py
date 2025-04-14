import sys
import heapq
from typing import *
from collections import OrderedDict
from collections import deque


class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def __add_to_tail(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def __remove_from_list(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = node.next = None

    def get(self, key: int) -> int:
        if node := self.map.get(key):
            self.__remove_from_list(node)
            self.__add_to_tail(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if node := self.map.get(key):
            node.val = value
            self.__remove_from_list(node)
        else:
            if len(self.map) == self.cap:
                node = self.head.next
                del self.map[node.key]
                self.__remove_from_list(node)
                del node
            node = self.map[key] = Node(key, value)
        self.__add_to_tail(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == "__main__":
    # solution = Solution()

    sys.exit(0)
