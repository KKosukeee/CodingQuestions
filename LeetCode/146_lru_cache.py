"""
Solution for 146. LRU Cache
https://leetcode.com/problems/lru-cache/
"""
class ListNode:
    """
    ListNode object
    """
    def __init__(self, key, val, next=None, prev=None):
        """
        Initialization method
        Args:
            key(int):
            val(int):
            next(ListNode):
            prev(ListNode):
        """
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    """
    Runtime: 236 ms, faster than 56.73% of Python3 online submissions for LRU Cache.
    Memory Usage: 23.3 MB, less than 6.06% of Python3 online submissions for LRU Cache.
    """
    def __init__(self, capacity):
        """
        Initialization method
        Args:
            capacity(int):
        """
        self.head, self.tail = None, None
        self.capacity, self.count = capacity, 0
        self.cache = {}

    def get(self, key):
        """
        Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1
        Args:
            key(int):

        Returns:

        """
        if not key in self.cache:
            return -1
        self.unlink_node(self.cache[key])
        self.update_tail(self.cache[key])
        return self.cache[key].val

    def put(self, key, value):
        """
        Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
        Args:
            key(int):
            value(int):

        Returns:

        """
        if not self.head:
            self.head = self.tail = ListNode(key, value)
            self.cache[key] = self.head
            self.count += 1
        elif key in self.cache:
            self.cache[key].val = value
            self.unlink_node(self.cache[key])
            self.update_tail(self.cache[key])
        else:
            if not self.count < self.capacity:
                del self.cache[self.head.key]
                self.unlink_node(self.head)
            node = ListNode(key, value, None, self.tail)
            self.update_tail(node)
            self.cache[key] = node
            self.count += 1

    def unlink_node(self, node):
        """
        Remove a link to the node
        Args:
            node(ListNode):

        Returns:

        """
        if node is self.head:
            if self.head.next:
                self.head.next.prev = None
                self.head = node.next
            else:
                self.head = node
        if node is self.tail:
            if self.tail.prev:
                self.tail.prev.next = None
                self.tail = node.prev
            else:
                self.tail = node
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.next, node.prev = None, None

    def update_tail(self, node):
        """
        Updates the tail with the node
        Args:
            node(ListNode):

        Returns:

        """
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
